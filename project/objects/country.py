
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
