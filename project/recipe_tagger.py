from langcodes import Language
from objects.receipe import Recipe
from modules.origin_extractor import OriginExtractor
from modules.label_extractor import LabelExtractor
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

    def run_pipeline(self, recipe: Recipe):
        # Add Modules here:

        # Origin Extractor - Returns the updated receipe and the wikipedia code of
        # the origin language
        updated_receipe, wiki_code = self.origin_extractor.run(recipe=recipe)

        updated_receipe = self.wiki_api.run(
            recipe=updated_receipe, wiki_code=wiki_code)

        updated_receipe = self.wiki_translator.run(
            recipe=updated_receipe, wiki_code=wiki_code)

        # change
        updated_receipe.wiki_description = recipe.description

        updated_receipe = self.label_extractor.run(recipe=updated_receipe)
        # TODO: Label Finalizer

        return updated_receipe
