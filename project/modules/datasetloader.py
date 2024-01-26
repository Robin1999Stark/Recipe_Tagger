import nltk
import spacy
from spacy.language import Language

# needs download of en_core_web_sm from spacy
# python -m spacy download en_core_web_sm


class DatasetLoader:
    def __init__(self):
        pass

    def load_data(self) -> Language:
        # Load Datasets here
        print("Loading Datasets...")
        nltk.download('punkt')
        nlp = spacy.load("en_core_web_md")
        print("Datasets Loaded\n")
        return nlp
