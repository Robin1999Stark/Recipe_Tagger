from spacy.language import Language
from objects.receipe import Recipe
from objects.country import Country
from objects.recipe_label import RecipeLabel, LabelCategory, make_labels_distinct
from typing import List


class LabelFinalizer:
    def __init__(self, nlp: Language):
        self.nlp = nlp

    def add_extended_cuisine(self, labels: List[RecipeLabel]) -> List[RecipeLabel]:
        added_labels: List[RecipeLabel] = list()

        for label in labels:
            if label.category == LabelCategory.CUISINE:
                for key in Country.world_countries:
                    country = Country.languages_countries.get(label.title, '')[
                        0]
                    if country in Country.world_countries[key]:
                        added_labels.append(RecipeLabel(
                            key, LabelCategory.CUISINE))

        return make_labels_distinct(labels=added_labels)

    def add_dietary_preferences(self, labels: List[RecipeLabel]) -> List[RecipeLabel]:
        added_labels: List[RecipeLabel] = list()

        cat_list: List[LabelCategory] = [label.category for label in labels]

        if LabelCategory.MEAT not in cat_list:
            if LabelCategory.SEAFOOD in cat_list:
                added_labels.append(RecipeLabel(
                    'PESCETARIAN', LabelCategory.DIETARYPREFERENCE))
            else:
                added_labels.append(RecipeLabel(
                    'VEGETARIAN', LabelCategory.DIETARYPREFERENCE))

                if LabelCategory.ANIMAL not in cat_list:
                    added_labels.append(RecipeLabel(
                        'VEGAN', LabelCategory.DIETARYPREFERENCE))

        if LabelCategory.NUT not in cat_list:
            added_labels.append(RecipeLabel(
                'NUTFREE', LabelCategory.DIETARYPREFERENCE))

        if LabelCategory.STAMPLEFOOD not in cat_list:
            added_labels.append(RecipeLabel(
                'LOWCARB', LabelCategory.DIETARYPREFERENCE))

        return make_labels_distinct(labels=added_labels)

    def run(self, recipe: Recipe) -> Recipe:
        labels: List[RecipeLabel] = list()
        print("##############################################################")
        print("LABEL Finalizer")
        print("##############################################################\n")
        print("Starting Label Finalizer... \n")

        labels = labels + self.add_extended_cuisine(recipe.labels)

        labels = labels + self.add_dietary_preferences(recipe.labels)

        labels = labels + recipe.labels

        updated_recipe = Recipe(
            title=recipe.title, description=recipe.description, origin=recipe.origin, wiki_description=recipe.wiki_description, labels=labels)

        print("Finished Label Finalizer!")
        print("##############################################################\n")

        return updated_recipe
