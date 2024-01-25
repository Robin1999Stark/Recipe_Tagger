from enum import Enum


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

    def print(self):

        print('**************************************************')
        print(f'Recipe Label: {self.title}')
        print(f'Category: {self.category} \n')
        print('**************************************************')


def print_label(label: RecipeLabel):
    label.print()
