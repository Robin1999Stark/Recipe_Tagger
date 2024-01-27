from modules.datasetloader import DatasetLoader
from example_data import recipes_label_extractor
from modules.label_extractor_modules.food_extractor import FoodExtractor
from objects.recipe_label import RecipeLabel, print_label
import pandas as pd
import os
from spacy.language import Language
import json
from pprint import pprint
from spacy.tokens import DocBin
from tqdm import tqdm
import spacy

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Start program from this file
# Before running this program for the first time call:
# pipenv run python -m spacy download en_core_web_sm
# to download the spacy english dataset


def annotations_to_spacy(nlp: Language, path: str = 'annotations.json'):

    with open('annotations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    train_data = data['annotations']

    for i in train_data:
        if i[1]['entities'] == []:
            i[1]['entities'] = (0, 0, "OTHER")
        else:
            i[1]['entities'][0] = tuple(i[1]['entities'][0])

    pprint(train_data)

    db = DocBin()

    for text, annot in tqdm(train_data):
        doc = nlp.make_doc(text=text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label,
                                 alignment_mode="contract")
            if span is None:
                print("Skipping etnry")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc=doc)

    db.to_disk("./train.spacy")


if __name__ == '__main__':

    dl = DatasetLoader()
    nlp = dl.load_data()

    entity_names = ["MEAT",
                    "NAMEOFDISH",
                    "NUT",
                    "SWEETSANDSUGAR",
                    "FRUITS",
                    "SEAFOOD",
                    "OTHER",
                    "STAMPLEFOOD",
                    "VEGETABLESHERBS",
                    "ANIMAL"]

    # annotations_to_spacy(nlp=nlp)
    nlp1 = spacy.load(r"./output/model-best")

    for recipe in recipes_label_extractor:
        if recipe.wiki_description != "":
            doc = nlp1(recipe.wiki_description)
            labels = doc.ents
            print("Reicipe: " + recipe.title)
            for label in labels:
                if (label.label_ != "OTHER"):
                    print(label.label_ + " : " + str(label.ents[0]))
            print("_________________________________")

    # extractor = FoodExtractor(nlp=nlp)

    # for recipe in recipes_label_extractor:
    #    labels = extractor.run(text=recipe.wiki_description)
    #    for label in labels:
    #        print_label(label=label)
