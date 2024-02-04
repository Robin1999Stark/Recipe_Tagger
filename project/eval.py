from modules.datasetloader import DatasetLoader
from recipe_tagger import RecipeTagger
from eval_data import title_origin
from objects.eval import EvalData
from typing import List

if __name__ == '__main__':

    evaluation: List[EvalData] = []

    dl = DatasetLoader()
    nlp, nlp_model = dl.load_data()

    tagger = RecipeTagger(nlp=nlp, nlp_model=nlp_model)

    evaluation.append(tagger.origin_extractor.eval(test_data=title_origin))

    for ed in evaluation:
        ed.print()
