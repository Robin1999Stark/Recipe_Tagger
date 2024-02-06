from langcodes import Language
from objects.receipe import Recipe
from modules.origin_extractor import OriginExtractor
from modules.label_extractor import LabelExtractor
from modules.label_finalizer import LabelFinalizer
from modules.wiki_api import WikiApi
from modules.translator import WikiTranslator


class RecipeTagger:
    def __init__(self, nlp: Language, nlp_model: Language):
        self.nlp = nlp
        self.nlp_model = nlp_model
        self.origin_extractor = OriginExtractor(nlp=self.nlp)
        self.label_extractor = LabelExtractor(nlp=nlp, nlp_model=nlp_model)
        self.wiki_api = WikiApi()
        self.wiki_translator = WikiTranslator()
        self.label_finalizer = LabelFinalizer(nlp=nlp)

    def run_pipeline(self, recipe: Recipe):

        # Origin Extractor - Returns the updated receipe and the wikipedia code of
        # the origin language
        updated_receipe, wiki_code = self.origin_extractor.run(recipe=recipe)

        # Wiki Api call - with previous extracted wiki code, the recipe title is fetched
        # from the wikipedia api endpoint. The returned wiki descriptions language is
        # the extracted origin from the previous module.
        updated_receipe = self.wiki_api.run(
            recipe=updated_receipe, wiki_code=wiki_code)

        # Wiki Translator - the wiki description is translated into english.
        updated_receipe = self.wiki_translator.run(
            recipe=updated_receipe, wiki_code=wiki_code)

        updated_receipe.wiki_description = recipe.description

        # Label extractor - extracts labels from the wikipedia description.
        # Labels are extracted with a pretrained spacy ner model that is trained
        # for additional Tags for meal specific categories like meat, nut, fruits, etc.
        # the mentioned preparation methods are extracted as well, using a lemmatizer that
        # breaks the words to its root and a basic pattern matching with some
        # predefined preparation methods.

        updated_receipe = self.label_extractor.run(recipe=updated_receipe)

        # Label finalizer - completes label set with basic rules like italian -> mediteran
        updated_receipe = self.label_finalizer.run(recipe=updated_receipe)

        return updated_receipe
