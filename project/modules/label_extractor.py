from spacy.language import Language
from objects.receipe import Recipe
from modules.label_extractor_modules.food_extractor import FoodExtractor
from modules.label_extractor_modules.cuisine_extractor import CuisineExtractor
from objects.country import Country
from objects.recipe_label import RecipeLabel, LabelCategory
from modules.label_extractor_modules.cooking_method_extractor import CookingMethodExtractor
from typing import List


class LabelExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.meal_type_extractor = FoodExtractor(nlp=nlp)
        self.cuisine_extractor = CuisineExtractor(nlp=nlp)
        self.cooking_method_extractor = CookingMethodExtractor(nlp=nlp)

    def extract_cuisine(self, recipe: Recipe) -> List[RecipeLabel]:
        cuisine_labels = list()
        if (recipe.origin == "English" or recipe.origin == "British"):
            cuisine_labels = self.cuisine_extractor.run(
                recipe.wiki_description)
        else:
            cuisine_labels = [RecipeLabel(
                recipe.origin, LabelCategory.CUISINE)]

        return cuisine_labels

    def extract_cooking_method(self, recipe: Recipe) -> List[RecipeLabel]:
        cooking_method_labels_wiki = self.cooking_method_extractor.run(
            recipe.wiki_description)
        cooking_method_labels_descr = self.cooking_method_extractor.run(
            recipe.description)

        cooking_method_labels_title = self.cooking_method_extractor.run(
            recipe.title)

        labels = cooking_method_labels_wiki + \
            cooking_method_labels_title + cooking_method_labels_descr

        return labels

    def run(self, recipe: Recipe) -> Recipe:
        labels = list()
        print("##############################################################")
        print("LABEL EXTRACTOR")
        print("##############################################################\n")
        print("Starting Label Extractor... \n")

        labels = labels + self.meal_type_extractor.run("test")

        labels = labels + self.extract_cooking_method(recipe=recipe)

        labels = labels + self.extract_cuisine(recipe=recipe)

        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=labels)

        print("Finished Label Extractor!")
        print("##############################################################\n")

        return updated_recipe
