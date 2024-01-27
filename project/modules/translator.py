from translate import Translator
from objects.receipe import Recipe


class WikiTranslator:
    def __init__(self, to_lang: str = "en"):
        self.to_lang = to_lang

    def translate_to_english(self, text, source_language):
        try:
            translator = Translator(
                to_lang=self.to_lang, from_lang=source_language)
            translation = translator.translate(text)
            return translation
        except Exception as e:
            return f"Translation error: {str(e)}"

    def run(self, recipe: Recipe, wiki_code: str) -> Recipe:

        wiki_description = recipe.wiki_description

        if (wiki_description != ""):

            recipe.wiki_description = self.translate_to_english(
                wiki_description, wiki_code)

        return recipe
