# from project.objects.receipe import Receipe
import spacy
from spacy.language import Language
import langid
from collections import Counter
import re
import queue
from langdetect import detect_langs
from nltk.tokenize import word_tokenize
from typing import List
from country_named_entity_recognition import find_countries
# needs download of en_core_web_sm from spacy
# python -m spacy download en_core_web_sm


class Receipe:
    def __init__(self, title: str, description: str, origin: str, wiki_description: str, labels: list[str]):
        self.title = title
        self.description = description
        self.origin = origin
        self.wiki_description = wiki_description
        self.labels = labels

    def print(self):
        print('##################################################')
        print(f'Receipe: {self.title}')
        print(f'Description: {self.description}')
        print(f'Origin: {self.origin}')
        print(f'Wiki Description: {self.wiki_description}')
        print(f'Labels: {self.labels}')
        print('##################################################')


def create_languages_countries(countries_languages):

    languages_countries = {}

    for country, language in countries_languages.items():
        if language in languages_countries:
            languages_countries[language].append(country)
        else:
            languages_countries[language] = [country]

    return languages_countries


class Country:

    languages_wiki = {
        "English": "en",
        "German": "de",
        "French": "fr",
        "Spanish": "es",
        "Japanese": "ja",
        "Russian": "ru",
        "Latn": "pt",
        "Italian": "it",
        "Chinese": "zh",
        "Persian": "fa",
        "Polish": "pl",
        "Dutch": "nl",
        "Arabic": "ar",
        "Ukrainian": "uk",
        "Hebrew": "he",
        "Turkish": "tr",
        "Indonesian": "id",
        "Czech": "cs",
        "Swedish": "sv",
        "Korean": "ko",
        "Vietnamese": "vi",
        "Hungarian": "hu",
        "Finnish": "fi",
        "Hindi": "hi",
        "Norwegian": "no",
        "Catalan": "ca",
        "Thai": "th",
        "Greek": "el",
        "Bengali": "bn",
        "Romanian": "ro",
        "Serbian": "sr",
        "Danish": "da",
        "Bulgarian": "bg",
        "Malay": "ms",
        "Azerbaijani": "az",
        "Estonian": "et",
        "Slovak": "sk",
        "Armenian": "hy",
        "Uzbek": "uz",
        "Croatian": "hr",
        "Basque": "eu",
        "Slovene": "sl",
        "Lithuanian": "lt",
        "Latvian": "lv",
        "Esperanto": "eo",
        "Belarusian": "be",
        "Urdu": "ur",
        "Kazakh": "kk",
        "Tamil": "ta",
        "Georgian": "ka",
    }
    langid_languages = {
        "af": "Afrikaans",
        "an": "Aragonese",
        "ar": "Arabic",
        "as": "Assamese",
        "az": "Azerbaijani",
        "be": "Belarusian",
        "bg": "Bulgarian",
        "bn": "Bengali",
        "br": "Breton",
        "bs": "Bosnian",
        "ca": "Catalan",
        "cs": "Czech",
        "cy": "Welsh",
        "da": "Danish",
        "de": "German",
        "dz": "Dzongkha",
        "el": "Greek",
        "en": "English",
        "eo": "Esperanto",
        "es": "Spanish",
        "et": "Estonian",
        "eu": "Basque",
        "fa": "Persian",
        "fi": "Finnish",
        "fo": "Faroese",
        "fr": "French",
        "ga": "Irish",
        "gl": "Galician",
        "gu": "Gujarati",
        "he": "Hebrew",
        "hi": "Hindi",
        "hr": "Croatian",
        "ht": "Haitian",
        "hu": "Hungarian",
        "hy": "Armenian",
        "id": "Indonesian",
        "is": "Icelandic",
        "it": "Italian",
        "ja": "Japanese",
        "jv": "Javanese",
        "ka": "Georgian",
        "kk": "Kazakh",
        "km": "Khmer",
        "kn": "Kannada",
        "ko": "Korean",
        "ku": "Kurdish",
        "ky": "Kyrgyz",
        "la": "Latin",
        "lb": "Luxembourgish",
        "lo": "Lao",
        "lt": "Lithuanian",
        "lv": "Latvian",
        "mg": "Malagasy",
        "mk": "Macedonian",
        "ml": "Malayalam",
        "mn": "Mongolian",
        "mr": "Marathi",
        "ms": "Malay",
        "mt": "Maltese",
        "nb": "Burmese",
        "ne": "Nepali",
        "nl": "Dutch",
        "no": "Norwegian",
        "oc": "Occitan",
        "or": "Oriya",
        "pa": "Punjabi",
        "pl": "Polish",
        "ps": "Pashto",
        "pt": "Portuguese",
        "qu": "Quechua",
        "ro": "Romanian",
        "ru": "Russian",
        "rw": "Kinyarwanda",
        "se": "Sinhala",
        "sk": "Slovak",
        "sl": "Slovenian",
        "sq": "Albanian",
        "sr": "Serbian",
        "sv": "Swedish",
        "sw": "Swahili",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tl": "Tagalog",
        "tr": "Turkish",
        "ug": "Uighur",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "vo": "Volapük",
        "wa": "Walloon",
        "xh": "Xhosa",
        "zh": "Chinese",
        "zu": "Zulu"
    }
    countries_languages = {
        "England": "English",
        "Germany": "German",
        "France": "French",
        "Spain": "Spanish",
        "Japan": "Japanese",
        "Russia": "Russian",
        "Portugal": "Latn",
        "Italy": "Italian",
        "China": "Chinese",
        "Iran": "Persian",
        "Poland": "Polish",
        "Netherlands": "Dutch",
        "Arab World": "Arabic",
        "Ukraine": "Ukrainian",
        "Israel": "Hebrew",
        "Turkey": "Turkish",
        "Indonesia": "Indonesian",
        "Czech Republic": "Czech",
        "Sweden": "Swedish",
        "South Korea": "Korean",
        "Vietnam": "Vietnamese",
        "Hungary": "Hungarian",
        "Finland": "Finnish",
        "India": "Hindi",
        "Norway": "Norwegian",
        "Catalonia": "Catalan",
        "Thailand": "Thai",
        "Greece": "Greek",
        "Bangladesh": "Bengali",
        "Romania": "Romanian",
        "Serbia": "Serbian",
        "Denmark": "Danish",
        "Bulgaria": "Bulgarian",
        "Malaysia": "Malay",
        "Azerbaijan": "Azerbaijani",
        "Estonia": "Estonian",
        "Slovakia": "Slovak",
        "Armenia": "Armenian",
        "Uzbekistan": "Uzbek",
        "Croatia": "Croatian",
        "Basque Country": "Basque",
        "Slovenia": "Slovene",
        "Lithuania": "Lithuanian",
        "Latvia": "Latvian",
        "Esperanto": "Esperanto",
        "Belarus": "Belarusian",
        "Pakistan": "Urdu",
        "Kazakhstan": "Kazakh",
        "Tamil Nadu": "Tamil",
        "Georgia": "Georgian",
    }

    languages_countries = create_languages_countries(
        countries_languages=countries_languages)

    def __init__(self, name: str):
        self.name = name
        self.lang = Country.countries_languages[name]
        self.wiki_code = Country.languages_wiki[self.lang]

    def get_wiki_code(self):
        Country.languages_wiki[self.lang]


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
    def __init__(self, receipe: Receipe, nlp: Language, ignore_lan=Country("England")):
        self.receipe = receipe
        self.nlp = nlp
        self.ignore_lan = ignore_lan

        self.extract_countries = extract_countries
        self.extract_countries_from_language = extract_countries_from_language
        self.max_pool_country = max_pool_country

    def run(self) -> Receipe:

        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        title = preprocess_input(self.receipe.title)
        description = preprocess_input(self.receipe.description)

        # Extract countries
        countries_from_title = self.extract_countries(text=title)
        countries_from_description = self.extract_countries(text=description)
        countries = countries_from_title + countries_from_description

        if (len(countries) > 0):

            best_country = self.max_pool_country(countries=countries)

            updated_receipe = Receipe(
                title=self.receipe.title, description=self.receipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Label Extractor!")
            print("##############################################################\n")

            return updated_receipe, best_country.get_wiki_code()

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

            updated_receipe = Receipe(
                title=self.receipe.title, description=self.receipe.description, origin=best_country.lang, wiki_description="", labels=[])

            print("Finished Label Extractor!")
            print("##############################################################\n")

            return updated_receipe, best_country.get_wiki_code()

        # If nothing is found return the standard language (English)
        updated_receipe = Receipe(
            title=self.receipe.title, description=self.receipe.description, origin=self.ignore_lan.lang, wiki_description="", labels=[])

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_receipe, self.ignore_lan.get_wiki_code()
