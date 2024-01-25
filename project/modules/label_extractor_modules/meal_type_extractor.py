from spacy.language import Language
from objects.receipe import Recipe
from typing import List
from objects.recipe_label import RecipeLabel, LabelCategory, print_label


class MealTypeExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp

    def run(self, text: str) -> List[RecipeLabel]:

        labels = list()
        print("##############################################################")
        print("Submodule: MEAL TYPE EXTRACTOR")
        print("##############################################################\n")
        print("Starting MEAL TYPE EXTRACTOR... \n")
        label = RecipeLabel("Alcohol", LabelCategory.ATTRIBUTE)
        labels.append(label)
        print("Finished MEAL TYPE EXTRACTOR!")
        print("##############################################################\n")
        return labels
