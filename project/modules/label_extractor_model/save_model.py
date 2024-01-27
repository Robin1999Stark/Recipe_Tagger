import spacy
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

if __name__ == '__main__':
    loaded_nlp = spacy.load("./output/model-best")
    loaded_nlp.to_bytes()
