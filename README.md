# Recipe Auto Tagger

This project was created in my universities `NLP` course. The use case of this project is to auto tag recipes using various NLP techniques
(mainly NER) to automatically create tags for a recipe. The recipe gets needs a title and a short description in order to get the tags.
The system consists of a pipeline with multiple modules, where each of them adds its categorized recipe tags. The main idea is to first extract
the possibly highest result for the recipes origin country and to call the Wikipedia API to get a more detailed description. This description is
then used to extract different tags such as cuisine, preperation methods, dietary preferences and much more.

## Modules in the Pipeline
- [x] **Label Extractor**
- [x] **Origin Extractor**
- [x] **Label Finalizer**
- [x] **Translator To English**
- [x] **Wikipedia API Call**

## Dependencies
  - needs download of `en_core_web_md` from spacy

        pipenv run python -m spacy download en_core_web_md

  - if model training is needed, download `en_core_web_lg` from spacy

        pipenv run python -m spacy download en_core_web_lg

  - needs to download the Pipenv from the Pipfile: navigate to `project` folder and run:
    
        pipenv install to install dependencies


## Split text 
Split text into one sentence per line. Is needed for the Tecoholic anotator: https://tecoholic.github.io/ner-annotator/
  - navigate to `label_extractor_model` folder and run:
    
        pipenv run python create_all_recipes.py
    

## Preprocess Dataset
  - navigate to `label_extractor_model` folder and run:
    
        pipenv run python preprocess.py
    
    This command creates the `train.spacy` and the `dev.spacy` files that are the splitted train and test data for the model in spacy format.

## Update Config
  - navigate to `label_extractor_model` folder and run:
    
        pipenv run python -m spacy init fill-config base_config.cfg config.cfg
    
    This command creates the `config.spacy` from the `base_config.spacy` file. Only use this if there is a need to update the config.


## Train Model
  - navigate to `label_extractor_model` folder and run:
    
        pipenv run python train.py
    
    This command trains the model. Keep in mind that the `en_core_web_lg` package from spacy is needed for this action.

## Use Model
  - After training the model, the best performing model can be found in the `output` folder und `mode-best`
  - the `output` folder is added to gitignore. Models are too big for commit.


## Run
  - navigate to `project` folder and run:
    
        pipenv run python main.py
