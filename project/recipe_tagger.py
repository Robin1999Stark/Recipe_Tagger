from langcodes import Language
from objects.receipe import Recipe
from modules.origin_extractor import OriginExtractor
from wikipedia import wikipedia, exceptions as wiki_exceptions
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

        wiki_article = get_wikipedia_article(wiki_code, updated_receipe.title)

        wiki_article = translate_to_english(wiki_article, wiki_code)
        updated_receipe = Recipe(title=updated_receipe.title, description=updated_receipe.description,
                                 origin=updated_receipe.origin, wiki_description=wiki_article, labels=updated_receipe.labels)
        # TODO: Label Extractor
        updated_receipe = self.label_extractor.run(recipe=updated_receipe)
        # TODO: Label Finalizer

        return updated_receipe


def get_wikipedia_article(language, term):
    wikipedia.set_lang(language)
    try:
        search_array = wikipedia.search(term)
        if (len(search_array) > 0):
            summary = wikipedia.summary(search_array[0])
            return summary
        return ""

    except wiki_exceptions.PageError as e:
        print(f"PageError: {e}")
        return ""


def translate_to_english(text, source_language):
    try:
        translator = Translator(to_lang="en", from_lang=source_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {str(e)}"
