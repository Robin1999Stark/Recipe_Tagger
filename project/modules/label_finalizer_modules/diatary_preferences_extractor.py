from objects import country


def finalizeTags(recipe):
    for label in recipe.labels:
        for key in world_countries:
            if label in world_countries[key]:
                recipe.labels.append(key)
    recipe.labels = list(set(recipe.labels))  # removes duplicates
    if 'MEAT' not in recipe.labels:
        recipe.labels.append('VEGETARIAN')
        if 'ANIMAL' not in recipe.labels:
            recipe.labels.append('VEGAN')
        if 'SEAFOOD' in recipe.labels:
            recipe.labels.append('PESCETARIAN')
    if 'NUT' not in recipe.labels:
        recipe.labels.append('NUTFREE')
    if 'STAMPLEFOOD' not in recipe.labels:
        recipe.labels.append('LOWCARB')
