from objects.receipe import Receipe
from modules.label_extractor import LabelExtractor


def run_pipeline(receipe: Receipe) -> Receipe:
    # Add Modules here:

    # TODO: Origin Extractor

    # TODO: Wiki Api Call

    # TODD: Translate to english

    # TODO: Label Extractor
    label_extractor = LabelExtractor(receipe=receipe)
    updated_receipe = label_extractor.run()
    # TODO: Label Finalizer

    return updated_receipe


def print_receipe(receipe: Receipe):
    receipe.print()


if __name__ == '__main__':
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

    updated_receipe = run_pipeline(receipe=receipe)

    print(updated_receipe)
