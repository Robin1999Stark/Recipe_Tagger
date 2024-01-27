from wikipedia import wikipedia, exceptions as wiki_exceptions
from objects.receipe import Recipe


class WikiApi:
    def __init__(self):
        pass

    def get_wikipedia_article(self, language: str, term: str):
        wikipedia.set_lang(language)
        try:
            search_array = wikipedia.search(term)
            if (len(search_array) > 0):
                summary = wikipedia.summary(search_array[0])
                return summary
            return ""

        except wiki_exceptions.PageError as e:
            print(f"PageError: {e}")
            return ""

    def run(self, recipe: Recipe, wiki_code: str) -> Recipe:

        if (recipe.title != ""):
            wiki_article = self.get_wikipedia_article(wiki_code, recipe.title)
            recipe.wiki_description = wiki_article

        return recipe
