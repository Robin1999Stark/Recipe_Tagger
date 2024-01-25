from spacy.language import Language
from objects.receipe import Recipe
from modules.label_extractor_modules.meal_type_extractor import MealTypeExtractor
from modules.label_extractor_modules.cuisine_extractor import CuisineExtractor


class LabelExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.meal_type_extractor = MealTypeExtractor(nlp=nlp)
        self.cuisine_extractor = CuisineExtractor(nlp=nlp)

    def run(self, recipe: Recipe) -> Recipe:

        labels = list()
        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        labels = labels + self.meal_type_extractor.run("test")

        labels = labels + self.cuisine_extractor.run(
            recipe.wiki_description + " " + recipe.description + " " + recipe.title)
        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=labels)

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe
