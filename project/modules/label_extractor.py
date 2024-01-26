from spacy.language import Language
from objects.receipe import Recipe
from modules.label_extractor_modules.meal_type_extractor import MealTypeExtractor
from modules.label_extractor_modules.cuisine_extractor import CuisineExtractor
from objects.country import Country
from objects.recipe_label import RecipeLabel, LabelCategory


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

        cuisine_labels = list()
        if (recipe.origin == "English" or recipe.origin == "British"):
            cuisine_labels = self.cuisine_extractor.run(
                recipe.wiki_description)
        else:
            cuisine_labels = [RecipeLabel(
                recipe.origin, LabelCategory.CUISINE)]

        labels = labels + cuisine_labels

        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=labels)

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe
