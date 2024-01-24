

class Recipe:
    def __init__(self, title: str, description: str, origin: str, wiki_description: str, labels: list[str]):
        self.title = title
        self.description = description
        self.origin = origin
        self.wiki_description = wiki_description
        self.labels = labels

    def print(self):

        print('**************************************************')
        print(f'Recipe Title: {self.title}')
        print('**************************************************')
        print(f'Recipe Description: {self.description} \n')
        print(f'Origin Language: {self.origin} \n')
        print(f'Wiki Description: {self.wiki_description} \n')
        print(f'Tags: {self.labels}')
        print('**************************************************')


def print_receipe(receipe: Recipe):
    receipe.print()
