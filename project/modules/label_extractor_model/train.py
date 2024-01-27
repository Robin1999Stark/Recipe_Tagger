from spacy.cli.train import train
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# train needs the en_core_web_lg package
if __name__ == '__main__':
    train(config_path="./config.cfg", output_path="./output", overrides={
          "paths.train": "./train.spacy", "paths.dev": "./dev.spacy"})
