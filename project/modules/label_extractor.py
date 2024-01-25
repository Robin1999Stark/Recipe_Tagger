from spacy.language import Language
from objects.receipe import Recipe
from modules.label_extractor_modules.meal_type_extractor import MealTypeExtractor


class LabelExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.meal_type_extractor = MealTypeExtractor(nlp=nlp)

    def run(self, recipe: Recipe) -> Recipe:

        labels = list()
        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        labels = labels + self.meal_type_extractor.run("test")

        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=labels)

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe
