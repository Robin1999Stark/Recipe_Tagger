import os
from spacy.language import Language
import json
from pprint import pprint
from spacy.tokens import DocBin
from tqdm import tqdm
import spacy
from io import TextIOWrapper
from sklearn.model_selection import train_test_split

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)


def annotations_to_spacy(nlp: Language, data: any, output: str = './train.spacy'):
    try:
        for i in data:
            if i[1]['entities'] == []:
                i[1]['entities'] = (0, 0, "OTHER")
            else:
                i[1]['entities'][0] = tuple(i[1]['entities'][0])

        pprint(data)

        db = DocBin()

        for text, annot in tqdm(data):
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

        db.to_disk(output)
        print(f"{output} was successfully created!")

    except Exception as e:
        print(e)
        print("annotations.json needs to be in the same directory as this file")


def preprocess(nlp: Language, path: str = 'annotations.json'):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data_annotaions = data['annotations']

    train_data, test_data = train_test_split(
        data_annotaions, test_size=0.2, random_state=42)

    annotations_to_spacy(nlp=nlp, data=train_data,
                         output='./train.spacy')

    annotations_to_spacy(nlp=nlp, data=test_data,
                         output='./dev.spacy')


# preprocess needs the en_core_web_sm package
if __name__ == '__main__':
    nlp = spacy.load("en_core_web_md")
    preprocess(nlp=nlp)
