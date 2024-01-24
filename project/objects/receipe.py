

class Recipe:
    def __init__(self, title: str, description: str, origin: str, wiki_description: str, labels: list[str]):
        self.title = title
        self.description = description
        self.origin = origin
        self.wiki_description = wiki_description
        self.labels = labels

    def print(self):
        print('##################################################')
        print(f'Receipe: {self.title}')
        print(f'Description: {self.description}')
        print(f'Origin: {self.origin}')
        print(f'Wiki Description: {self.wiki_description}')
        print(f'Labels: {self.labels}')
        print('##################################################')


def print_receipe(receipe: Recipe):
    receipe.print()
