from spacy.language import Language
from collections import Counter
import re
from langdetect import detect_langs
from nltk.tokenize import word_tokenize
from typing import List
from country_named_entity_recognition import find_countries
from objects.receipe import Recipe
from objects.country import Country
from objects.eval import EvalData
from metrics.metrics import accuracy_score, precision_score, recall_score, f1_score


def extract_multi_word_phrases(sentence: str, nlp: Language):
    # Process the input sentence using spaCy
    doc = nlp(sentence)

    phrases = [chunk.text for chunk in doc.noun_chunks]

    return phrases


def remove_whitespace_sequences(text: str):
    whitespace_pattern = re.compile(r'\s+')
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


def extract_countries_from_language(text: str, nlp, standard_lang_id="en") -> List[Country]:

    multi_word_phrases = extract_multi_word_phrases(text, nlp=nlp)
    countries_conf = list()

    for word_phrase in multi_word_phrases:
        langs = detect_langs(text=word_phrase)

        for lang_info in langs:
            lang = lang_info.lang
            conf = lang_info.prob
            if (conf > 0.9 and lang != standard_lang_id):
                country_name = Country.languages_countries.get(
                    Country.langid_languages.get(lang, ""), [""])[0]
                if country_name:
                    country = Country(country_name)
                    countries_conf.append((country, conf))

    return [c[0] for c in countries_conf]


def extract_countries(text) -> List[Country]:

    extracted_countries = find_countries(text=text,
                                         is_ignore_case=True,
                                         is_georgia_probably_the_country=True)

    countries = list()

    for c in extracted_countries:
        country_name = c[0].name
        if country_name in Country.countries_languages:
            country = Country(c[0].name)
            countries.append(country)

    return countries


def extract_countries_from_norp(text, nlp: Language) -> List[Country]:
    doc = nlp(text)

    norp_entities = [ent.text for ent in doc.ents if ent.label_ == "NORP"]

    countries = list()
    for norp in norp_entities:
        country_name = Country.norp_country.get(norp, "")
        if country_name:
            countries.append(Country(country_name))

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
        self.extract_countries_from_norp = extract_countries_from_norp
        self.extract_countries_from_language = extract_countries_from_language
        self.max_pool_country = max_pool_country

    def eval(self, test_data: List[Recipe]) -> EvalData:
        y_true = []
        y_pred = []
        for td in test_data:
            lang = Country.get_unique_lang_(td.origin)
            y_true.append(lang)
            return_recipe = self.run(
                recipe=Recipe(td.title, td.description))[0]
            y_pred.append(return_recipe.origin)

        ac = accuracy_score(y_pos=y_true, y_pred=y_pred)
        pre = precision_score(y_pos=y_true, y_pred=y_pred)
        rec = recall_score(y_pos=y_true, y_pred=y_pred)
        f1 = f1_score(y_pos=y_true, y_pred=y_pred)

        return EvalData("Origin Extractor", accuracy=ac, precision=pre, recall=rec, f1_score=f1)

    def run(self, recipe: Recipe) -> Recipe:

        print("##############################################################")
        print("ORIGIN EXTRACTOR")
        print("##############################################################\n")
        print("Starting Origin Extractor... \n")

        title = preprocess_input(recipe.title)
        description = preprocess_input(recipe.description)

        # Extract countries
        countries_from_title = self.extract_countries(text=title)
        countries_from_description = self.extract_countries(text=description)
        countries = countries_from_title + countries_from_description

        if (len(countries) > 0):

            best_country = self.max_pool_country(countries=countries)

            updated_recipe = Recipe(
                title=recipe.title, description=recipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Origin Extractor!")
            print("##############################################################\n")

            return updated_recipe, best_country.wiki_code

        # Extract NORP with NER and get countries from it
        countries_norp_title = self.extract_countries_from_norp(
            text=title, nlp=self.nlp)
        countries_norp_description = self.extract_countries_from_norp(
            text=description, nlp=self.nlp)

        countries = countries_norp_title + countries_norp_description

        if (len(countries) > 0):

            best_country = self.max_pool_country(countries=countries)

            updated_recipe = Recipe(
                title=recipe.title, description=recipe.description, origin=best_country.lang, wiki_description=recipe.wiki_description, labels=recipe.labels)

            print("Finished Origin Extractor!")
            print("##############################################################\n")

            return updated_recipe, best_country.wiki_code

        # If nothing is found return the standard language (English)
        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=self.ignore_lan.lang, wiki_description=recipe.wiki_description, labels=recipe.labels)

        print("Finished Origin Extractor!")
        print("##############################################################\n")

        return updated_recipe, self.ignore_lan.wiki_code

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

            updated_recipe = Recipe(
                title=recipe.title, description=recipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Origin Extractor!")
            print("##############################################################\n")

            return updated_recipe, best_country.wiki_code
