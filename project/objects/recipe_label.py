from enum import Enum
from typing import List


class LabelCategory(Enum):

    INGREDIENT = "in"
    CUISINE = "cu"
    PREPARATIONMETHOD = "pm"
    MEALTYPE = "mt"
    DIETARYPREFERENCE = "dp"
    OCCASION = "oc"
    ATTRIBUTE = "at"


class RecipeLabel:
    def __init__(self, title: str, category: LabelCategory):
        self.title = title
        self.category = category

    def __eq__(self, other):
        return isinstance(other, RecipeLabel) and self.title == other.title and self.category == other.category

    def __hash__(self):
        return hash((self.title, self.category))

    def print(self):

        print('**************************************************')
        print(f'Recipe Label: {self.title}')
        print(f'Category: {self.category} \n')
        print('**************************************************')


def print_label(label: RecipeLabel):
    label.print()


def make_labels_destinct(labels: List[RecipeLabel]) -> List[RecipeLabel]:
    unique_labels = list(set(labels))
    return unique_labels
