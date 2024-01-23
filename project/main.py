from spacy.language import Language
from objects.receipe import Receipe
from modules.origin_extractor import OriginExtractor
from modules.datasetloader import DatasetLoader


def run_pipeline(receipe: Receipe, nlp: Language) -> Receipe:
    # Add Modules here:

    # Origin Extractor - Returns the updated receipe and the wikipedia code of
    # the origin language
    label_extractor = OriginExtractor(receipe=receipe, nlp=nlp)
    updated_receipe, wiki_code = label_extractor.run()

    # TODO: Wiki Api Call

    # TODD: Translate to english

    # TODO: Label Extractor

    # TODO: Label Finalizer

    return updated_receipe


def print_receipe(receipe: Receipe):
    receipe.print()


if __name__ == '__main__':

    dl = DatasetLoader()
    nlp = dl.load_data()

    receipe1 = Receipe("Spicy Garlic Shrimp Pasta Italian",
                       """
                        This Spicy Garlic Shrimp Pasta from Italy is a delightful fusion of bold flavors 
                        and comforting textures. Succulent shrimp are sautéed to perfection
                        in a spicy garlic-infused olive oil, creating a mouthwatering base 
                        for the pasta. The dish is then elevated with a medley of vibrant 
                        vegetables and a creamy Rome tomato sauce that perfectly balances the heat. 
                        Tossed with al dente linguine Toscana and garnished with fresh parsley and 
                        grated Parmesan, this dish is a celebration of both simplicity and 
                        sophistication. It's a quick and impressive recipe that will satisfy 
                        your cravings for a flavorful and satisfying meal.")
                    
                    """,
                       "",
                       "",
                       [])

    updated_receipe = run_pipeline(receipe=receipe1, nlp=nlp)

    print_receipe(updated_receipe)

    receipe2 = Receipe("Spaghetti Bolognese",
                       """
                        Spaghetti Bolognese is a classic Italian pasta dish.
                        It features a rich and savory meat sauce served over cooked spaghetti.
                        Garnish with grated Parmesan cheese and fresh basil for a delicious 
                        meal.                    
                        """,
                       "",
                       "",
                       [])

    updated_receipe = run_pipeline(receipe=receipe2, nlp=nlp)

    print_receipe(updated_receipe)
