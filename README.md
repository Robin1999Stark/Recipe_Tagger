# NLP_Receipe_auto_labeling

This is a project from the `NLP` course. The use case of this project is to auto tag recipes using 
NLP techniques like `NER` and other.

## Modules
- [ ] **Label Extractor**
- [x] **Origin Extractor**
- [ ] **Label Finalizer**
- [ ] **Wikipedia API Call**

## Dependencies
  - needs download of en_core_web_md from spacy

        pipenv run python -m spacy download en_core_web_md

  - needs to download the Pipenv from the Pipfile: navigate to `project` folder and run:
    
        pipenv install to install dependencies
       

## Run
  - navigate to `project` folder and run:
    
        pipenv run python main.py
