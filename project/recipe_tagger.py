from langcodes import Language
from objects.receipe import Recipe
from modules.origin_extractor import OriginExtror
import wikipediaapi
from translate import Translator
from modules.label_extractor import LabelExtractor



class RecipeTagger:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.origin_extractor = OriginExtractor(nlp=self.nlp)
        self.label_extractor = LabelExtractor(nlp=nlp)

    def run_pipeline(self, recipe: Recipe):
        # Add Modules here:

        # Origin Extractor - Returns the updated receipe and the wikipedia code of
        # the origin language
        updated_receipe, wiki_code = self.origin_extractor.run(recipe=recipe)

        wiki_article = get_wikipedia_article(wiki_code, updated_receipe)

        wiki_article = translate_to_english(wiki_article, wiki_code)

        # TODO: Label Extractor
        updated_receipe = self.label_extractor.run(recipe=updated_receipe)
        # TODO: Label Finalizer

        recipe = updated_receipe
        return updated_receipe + wiki_article


def get_wikipedia_article(language, term):
    wiki_wiki = wikipediaapi.Wikipedia('NLP_Test_Project (andreas.lieber@uni-a.de)', language)
    page_py = wiki_wiki.page(term)

    if not page_py.exists():
        return f"No Wikipedia article found for '{term}' in {language}."

    return page_py.text


def translate_to_english(text, source_language):
    try:
        translator = Translator(to_lang="en", from_lang=source_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {str(e)}"
