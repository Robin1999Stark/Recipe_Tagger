from spacy.cli.train import train


# train needs the en_core_web_lg package
if __name__ == '__main__':
    train("./config.cfg",
          overrides={"paths.train": "./train.spacy", "paths.dev": "./dev.spacy", "output": "./output"})
