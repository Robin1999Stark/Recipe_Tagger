from spacy.language import Language
from typing import List
from objects.recipe_label import RecipeLabel, LabelCategory, make_labels_distinct
from nltk.stem import WordNetLemmatizer

# Extracts The Cooking Method of different dishes


class CookingMethodExtractor:
    def __init__(self, nlp: Language):
        self.nlp = nlp
        self.lemmatizer = WordNetLemmatizer()
        self.all_cooking_methods = [
            "grill",
            "bake",
            "cook",
            "raw",
            "roast",
            "bake",
            "barbe",
            "smoke",
            "braise",
            "sauté",
            "saute",
            "blaunch",
            "fry",
            "steam",
            "boil",
            "simmer",
            "marinate",
            "pierce",
            "tenderize",
            "pound",
            "caramelize",
            "glaze",
            "age",
            "deglaze",
            "macerate",
            "ferment",
            "sear",
            "poach",
            "broil",
            "stew",
            "stir-fry",
            "pan-fry",
            "season"
        ]

    def run(self, text: str) -> List[RecipeLabel]:

        labels = list()

        doc = self.nlp(text=text)

        for sentence in doc.sents:
            labels = labels + \
                self.extract_cooking_method(sentence=sentence.text)

        return labels

    def extract_cooking_method(self, sentence: str) -> List[RecipeLabel]:
        doc = self.nlp(sentence)
        labels: List[RecipeLabel] = []

        for token in doc:
            stemmed_lemma = self.lemmatizer.lemmatize(token.lemma_.lower())
            if (stemmed_lemma in self.all_cooking_methods):
                if (
                    (token.pos_ == "VERB") or
                    (token.pos_ == "ADJ") or
                    (token.pos_ == "NOUN")
                ):
                    label = RecipeLabel(
                        stemmed_lemma, LabelCategory.PREPARATIONMETHOD)
                    labels.append(label)

        return make_labels_distinct(labels=labels)
