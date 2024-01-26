from langcodes import Language
from objects.receipe import Recipe
from modules.origin_extractor import OriginExtractor
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

        # TODO: Wiki Api Call

        # TODD: Translate to english

        # TODO: Label Extractor
        updated_receipe = self.label_extractor.run(recipe=updated_receipe)
        # TODO: Label Finalizer

        recipe = updated_receipe
        return updated_receipe
