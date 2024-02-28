# Recipe Auto Tagger

This project, developed during my university's Natural Language Processing (NLP) course, aims to automate the tagging of recipes using various NLP techniques, primarily Named Entity Recognition (NER). The system requires a recipe title and a brief description to generate tags automatically.

The architecture comprises multiple modules forming a pipeline, with each module contributing categorized recipe tags. The initial step involves extracting the most likely origin country for the recipe. Subsequently, the Wikipedia API is invoked to obtain a more detailed description, which serves as the basis for extracting diverse tags such as cuisine, preparation methods, dietary preferences, and more.

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
