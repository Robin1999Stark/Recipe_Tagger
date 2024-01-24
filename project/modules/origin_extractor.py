from spacy.language import Language
from collections import Counter
import re
from langdetect import detect_langs
from nltk.tokenize import word_tokenize
from typing import List
from country_named_entity_recognition import find_countries
from objects.receipe import Receipe
from objects.country import Country


def extract_multi_word_phrases(sentence, nlp):
    # Process the input sentence using spaCy
    doc = nlp(sentence)

    # Extract noun chunks (multi-word phrases)
    phrases = [chunk.text for chunk in doc.noun_chunks]

    return phrases


def remove_whitespace_sequences(text):
    # Define a regular expression pattern for matching whitespace sequences
    whitespace_pattern = re.compile(r'\s+')

    # Use sub() to replace matched sequences with a single space
    cleaned_text = re.sub(whitespace_pattern, ' ', text)

    return cleaned_text


def preprocess_input(text: str):
    text = remove_whitespace_sequences(text=text)
    tokenized_text = word_tokenize(text=text)

    joined_string = ' '.join(tokenized_text)
    return joined_string


def get_most_common_string(strings) -> str:
    counts = Counter(strings)
    most_common, _ = counts.most_common(1)[0]
    return most_common


def extract_countries_from_language(text: str, nlp, standard_lang_id="en"):

    multi_word_phrases = extract_multi_word_phrases(text, nlp=nlp)
    countries_conf = list()

    for word_phrase in multi_word_phrases:
        langs = detect_langs(text=word_phrase)

        for lang_info in langs:
            lang = lang_info.lang
            conf = lang_info.prob
            if (conf > 0.9 and lang != standard_lang_id):
                country_name = Country.languages_countries[Country.langid_languages[lang]][0]
                country = Country(country_name)
                countries_conf.append((country, conf))

    return [c[0] for c in countries_conf]


def extract_countries(text):

    extracted_countries = find_countries(text=text,
                                         is_ignore_case=True,
                                         is_georgia_probably_the_country=True)

    countries = list()
    for c in extracted_countries:
        country = Country(c[0].name)
        countries.append(country)

    return countries


def max_pool_country(countries: List[Country]) -> Country:
    country_counts = Counter(country.name for country in countries)
    max_country_name = max(country_counts, key=country_counts.get)
    max_country = next(
        country for country in countries if country.name == max_country_name)
    return max_country


class OriginExtractor:
    def __init__(self, nlp: Language, ignore_lan=Country("England")):
        self.nlp = nlp
        self.ignore_lan = ignore_lan
        self.extract_countries = extract_countries
        self.extract_countries_from_language = extract_countries_from_language
        self.max_pool_country = max_pool_country

    def run(self, recipe: Receipe) -> Receipe:

        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        title = preprocess_input(recipe.title)
        description = preprocess_input(recipe.description)

        # Extract countries
        countries_from_title = self.extract_countries(text=title)
        countries_from_description = self.extract_countries(text=description)
        countries = countries_from_title + countries_from_description

        if (len(countries) > 0):

            best_country = self.max_pool_country(countries=countries)

            updated_recipe = Receipe(
                title=recipe.title, description=recipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Label Extractor!")
            print("##############################################################\n")

            return updated_recipe, best_country.get_wiki_code()

        # Extract countries from text language
        countries_from_language_title = self.extract_countries_from_language(
            text=title, nlp=self.nlp)
        countries_from_language_description = self.extract_countries_from_language(
            text=description, nlp=self.nlp)
        countries_from_language = countries_from_language_title + \
            countries_from_language_description

        if (len(countries_from_language) > 0):

            best_country = self.max_pool_country(
                countries=countries_from_language)

            updated_recipe = Receipe(
                title=recipe.title, description=recipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Label Extractor!")
            print("##############################################################\n")

            return updated_recipe, best_country.get_wiki_code()

        # If nothing is found return the standard language (English)
        updated_recipe = Receipe(
            title=recipe.title, description=recipe.description, origin=self.ignore_lan.lang, wiki_description="", labels=[])

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe, self.ignore_lan.get_wiki_code()
