from spacy.language import Language
from typing import List
from objects.recipe_label import RecipeLabel, LabelCategory
import spacy
# Extracts Food Entities and ingredients


class FoodExtractor:
    def __init__(self, nlp: Language, nlp_model: Language):
        self.nlp = nlp
        self.nlp_model = nlp_model

    def run(self, text: str) -> List[RecipeLabel]:

        labels = list()
        print("##############################################################")
        print("Submodule: MEAL TYPE EXTRACTOR")
        print("##############################################################\n")
        print("Starting MEAL TYPE EXTRACTOR... \n")

        if text != "":
            doc = self.nlp_model(text=text)
            ent_labels = doc.ents
            for label in ent_labels:
                if (label.label_ != "OTHER"):
                    recipe_label = RecipeLabel(
                        str(label.ents), label.label_)
                    labels.append(recipe_label)

        print("Finished MEAL TYPE EXTRACTOR!")
        print("##############################################################\n")
        return labels
