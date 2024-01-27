from spacy.language import Language
from typing import List
from objects.recipe_label import RecipeLabel, LabelCategory, make_labels_destinct
from spacy.language import Language
from collections import Counter
import re
from nltk.tokenize import word_tokenize
from typing import List
from country_named_entity_recognition import find_countries
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


def extract_countries(text) -> List[RecipeLabel]:

    labels = list()
    extracted_countries = find_countries(text=text,
                                         is_ignore_case=True,
                                         is_georgia_probably_the_country=True)

    countries: List[Country] = list()
    for c in extracted_countries:
        country_name = Country.norp_country.get(c[0].name, "")
        if country_name:
            countries.append(Country(country_name))

    for country in countries:
        label = RecipeLabel(country.lang, LabelCategory.CUISINE)
        labels.append(label)

    return labels


def extract_countries_from_norp(text, nlp: Language) -> List[RecipeLabel]:
    labels = list()
    doc = nlp(text)

    norp_entities = [ent.text for ent in doc.ents if ent.label_ == "NORP"]

    countries = list()
    for norp in norp_entities:
        country_name = Country.norp_country.get(norp, "")
        if country_name:
            countries.append(Country(country_name))

    for country in countries:
        label = RecipeLabel(country.lang, LabelCategory.CUISINE)
        labels.append(label)

    return labels


def max_pool_country(countries: List[Country]) -> Country:
    country_counts = Counter(country.name for country in countries)
    max_country_name = max(country_counts, key=country_counts.get)
    max_country = next(
        country for country in countries if country.name == max_country_name)
    return max_country


class CuisineExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.extract_countries = extract_countries
        self.extract_countries_from_norp = extract_countries_from_norp
        self.max_pool_country = max_pool_country

    def run(self, text: str) -> List[RecipeLabel]:
        labels = list()

        processed_text = preprocess_input(text=text)

        labels_from_countries = self.extract_countries(text=processed_text)
        labels_from_norp = self.extract_countries_from_norp(nlp=self.nlp,
                                                            text=processed_text)

        labels = labels_from_countries + labels_from_norp

        return make_labels_destinct(labels=labels)
