import nltk
import spacy
from spacy.language import Language


import os


current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
# needs download of en_core_web_sm from spacy
# python -m spacy download en_core_web_sm


class DatasetLoader:
    def __init__(self):
        pass

    def load_data(self) -> Language:
        # Load Datasets here
        print("Loading Datasets...")
        nltk.download('punkt')
        nltk.download('wordnet')
        nlp = spacy.load("en_core_web_md")
        nlp_model = spacy.load(
            r"./label_extractor_model/output/model-best")
        print("Datasets Loaded\n")
        return nlp, nlp_model
