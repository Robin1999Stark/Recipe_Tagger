import spacy
from spacy.language import Language
from objects.receipe import Receipe
from modules.origin_extractor import OriginExtractor
import nltk


def run_pipeline(receipe: Receipe, nlp: Language) -> Receipe:
    # Add Modules here:

    # TODO: Origin Extractor

    # TODO: Wiki Api Call

    # TODD: Translate to english

    # TODO: Label Extractor
    label_extractor = OriginExtractor(receipe=receipe)
    updated_receipe = label_extractor.run(nlp=nlp)
    # TODO: Label Finalizer

    return updated_receipe


def print_receipe(receipe: Receipe):
    receipe.print()


if __name__ == '__main__':

    # Load Datasets here
    print("Loading Datasets...")
    nltk.download('punkt')
    nlp = spacy.load("en_core_web_md")
    print("Dataset Loaded\n")

    receipe = Receipe("Spicy Garlic Shrimp Pasta Italian",
                      """
                        This Spicy Garlic Shrimp Pasta is a delightful fusion of bold flavors 
                        and comforting textures. Succulent shrimp are sautéed to perfection
                        in a spicy garlic-infused olive oil, creating a mouthwatering base 
                        for the pasta. The dish is then elevated with a medley of vibrant 
                        vegetables and a creamy tomato sauce that perfectly balances the heat. 
                        Tossed with al dente linguine and garnished with fresh parsley and 
                        grated Parmesan, this dish is a celebration of both simplicity and 
                        sophistication. It's a quick and impressive recipe that will satisfy 
                        your cravings for a flavorful and satisfying meal.")
                    
                    """,
                      "",
                      "",
                      [])

    updated_receipe = run_pipeline(receipe=receipe, nlp=nlp)

    print(updated_receipe)
