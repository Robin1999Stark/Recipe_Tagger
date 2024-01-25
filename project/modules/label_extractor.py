from spacy.language import Language
from objects.receipe import Recipe


class LabelExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp

    def run(self, recipe: Recipe) -> Recipe:

        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=[])

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe, self.ignore_lan.get_wiki_code()
