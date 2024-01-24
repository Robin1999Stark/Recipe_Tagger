from objects.receipe import print_receipe
from modules.datasetloader import DatasetLoader
from example_data import recipes
from recipe_tagger import RecipeTagger

# Start program from this file
# Before running this program for the first time call:
# pipenv run python -m spacy download en_core_web_sm
# to download the spacy english dataset

if __name__ == '__main__':

    dl = DatasetLoader()
    nlp = dl.load_data()

    tagger = RecipeTagger(nlp=nlp)

    for recipe in recipes:
        updated_receipe = tagger.run_pipeline(recipe=recipe)
        print_receipe(updated_receipe)
