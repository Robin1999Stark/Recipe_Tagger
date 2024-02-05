from objects.receipe import Recipe
from objects.recipe_label import RecipeLabel, LabelCategory


class TitleOrg():
    def __init__(self, title: str, description: str, origin: str):
        self.title = title
        self.description = description
        self.origin = origin


title_origin = [
    Recipe(
        title="Poulet Reine Elizabeth",
        description="Poulet Reine Elizabeth, a classic French dish, showcases the culinary artistry of tender chicken breasts smothered in a velvety Mornay sauce enriched with mushrooms and creamy béchamel. Named in honor of Queen Elizabeth II, this elegant and flavorful poultry creation exemplifies French gastronomy, offering a delightful harmony of textures and tastes.",
        origin="French"
    ),
    Recipe(
        title="Pizza",
        description="Pizza is a beloved and versatile dish originating from Italy, featuring a thin or thick crust topped with a savory tomato sauce, melted cheese, and a variety of flavorful ingredients such as pepperoni, vegetables, and herbs. Its irresistible combination of crispy crust, gooey cheese, and an array of toppings makes pizza a universally cherished comfort food enjoyed worldwide.",
        origin="Italian"
    ),
    Recipe(
        title="Spaghetti Bolognese",
        description="A comforting Italian classic, spaghetti Bolognese features al dente pasta smothered in a rich, slow-cooked tomato and meat sauce, creating a hearty and satisfying meal.",
        origin="Italian"
    ),
    Recipe(
        title="Chicken Alfredo",
        description="Succulent grilled chicken meets creamy Alfredo sauce in this indulgent pasta dish, marrying tender protein with velvety pasta perfection.",
        origin="English"
    ),
    Recipe(
        title="Vegetarian Stir-Fry",
        description="A comforting Italian classic, spaghetti Bolognese features al dente pasta smothered in a rich, slow-cooked tomato and meat sauce, creating a hearty and satisfying meal.",
        origin="Italian"
    ),
    Recipe(
        title="Poutine",
        description="Poutine, a Canadian culinary delight, consists of crispy French fries topped with fresh cheese curds and drenched in savory brown gravy. This irresistible combination of textures and flavors creates a comforting and indulgent dish that has become a symbol of Canadian cuisine.",
        origin="English"
    ),
    Recipe(
        title="Wonton",
        description="Wontons are delicate Chinese dumplings, typically made by wrapping seasoned minced meat, such as pork or shrimp, in thin sheets of dough. These little parcels are then boiled, steamed, or fried, resulting in bite-sized pockets of savory goodness enjoyed in soups or as appetizers, showcasing the artful simplicity of Chinese culinary craftsmanship.",
        origin="Chinese"
    ),
    Recipe(
        title="Taco",
        description="Tacos are a Mexican culinary treasure, featuring a folded or rolled tortilla filled with a variety of savory ingredients such as seasoned meats, beans, lettuce, cheese, and salsa. The diverse combination of flavors and textures in each taco, often accompanied by a squeeze of lime, offers a handheld delight that has become a global favorite, celebrated for its versatility and delicious simplicity.",
        origin="Mexican"
    ),
    Recipe(
        title="Pierogi",
        description="Pierogi, a beloved Eastern European dish, hails from Poland and holds a special place in its culinary tradition. These dumplings are filled with a delectable mixture of ingredients like potatoes, cheese, meat, or sauerkraut. Typically boiled or fried, pierogi are enjoyed throughout the region, with variations found in countries such as Ukraine and Russia. Served with toppings like sour cream, onions, or butter, pierogi offer a satisfying and versatile comfort food experience.",
        origin="Ukranian"
    ),
    Recipe(
        title="Mashed potato",
        description="Creamy and comforting, mashed potatoes are a staple in American cuisine, often gracing tables during holiday feasts and everyday meals alike. Potatoes are boiled, mashed, and whipped with butter and milk, creating a velvety side dish that perfectly complements a variety of main courses, showcasing the timeless appeal of this classic comfort food in the United States and beyond.",
        origin="English"
    ),
    Recipe(
        title="Roti canai",
        description="Roti canai is a popular Malaysian and Indian dish, featuring thin, flaky, and stretchy flatbread that is skillfully prepared by tossing and flipping the dough. Served with flavorful curries or dhal, this versatile and delicious flatbread has become a breakfast favorite and street food staple, symbolizing the rich culinary heritage of Malaysia and its South Asian influences.",
        origin="Malay"
    ),
    Recipe(
        title="Dosa",
        description="Dosa, a cherished South Indian delicacy, is a thin and crispy fermented rice and urad dal crepe. This versatile dish is enjoyed for breakfast or as a snack, often served with coconut chutney and tangy sambar. With its light texture and delightful taste, dosa exemplifies the diversity and depth of flavors found in Indian cuisine, particularly in the southern regions of the country.",
        origin="Hindi"
    ),
    Recipe(
        title="Chapati",
        description="Chapati, a staple in Indian cuisine, is a simple unleavened flatbread made from whole wheat flour, water, and a pinch of salt. Cooked on a hot griddle, chapati puffs up beautifully, becoming a soft and pliable bread that pairs perfectly with a variety of dishes. Whether served with curries, lentils, or used as a wrap, chapati is a versatile and integral part of Indian meals, reflecting the rich culinary traditions of the subcontinent.",
        origin="Hindi"
    ),
    Recipe(
        title="Crumble",
        description="Crumble, a classic dessert, showcases a delectable mix of sweet, spiced fruit filling topped with a crumbly mixture of flour, butter, and sugar. Baked to golden perfection, this comforting dish, often made with apples, berries, or stone fruits, delivers a delightful contrast between the warm, gooey interior and the crisp, buttery crumb topping, making it a beloved treat in British and American kitchens alike.",
        origin="English"
    ),
    Recipe(
        title="Knieperkohl",
        description="Knieperkohl is a traditional German dish, particularly popular in the region of Brandenburg. It consists of pickled cabbage, often combined with various vegetables and spices. This tangy and flavorful dish is typically enjoyed as a side dish or accompaniment, adding a distinctive taste to German meals and reflecting the country's rich culinary heritage.",
        origin="German"
    )
]


data = [
    Recipe("Poulet Reine Elizabeth",
           "Poulet Reine Elizabeth, a classic French dish, showcases the culinary artistry of tender chicken breasts smothered in a velvety Mornay sauce enriched with mushrooms and creamy béchamel. Named in honor of Queen Elizabeth II, this elegant and flavorful poultry creation exemplifies French gastronomy, offering a delightful harmony of textures and tastes.",
           "French",
           "",
           [
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("VEGETABLESHERBS", LabelCategory.VEGETABLESHERBS),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
               RecipeLabel("FRUITS", LabelCategory.FRUITS)
           ]),
    Recipe("Pizza",
           "Pizza is a beloved and versatile dish originating from Italy, featuring a thin or thick crust topped with a savory tomato sauce, melted cheese, and a variety of flavorful ingredients such as pepperoni, vegetables, and herbs. Its irresistible combination of crispy crust, gooey cheese, and an array of toppings makes pizza a universally cherished comfort food enjoyed worldwide.",
           "Italian",
           "",
           [
               RecipeLabel("ANIMAL", LabelCategory.ANIMAL),
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("VEGETABLESHERBS",
                           LabelCategory.VEGETABLESHERBS),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
           ]),
    Recipe("Spaghetti Bolognese",
           "A comforting Italian classic, spaghetti Bolognese features al dente pasta smothered in a rich, slow-cooked tomato and meat sauce, creating a hearty and satisfying meal.",
           "Italian",
           "",
           [
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("ANIMAL", LabelCategory.ANIMAL),
               RecipeLabel("VEGETABLESHERBS",
                           LabelCategory.VEGETABLESHERBS),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
           ]),
    Recipe("Chicken Alfredo",
           "Succulent grilled chicken meets creamy Alfredo sauce in this indulgent pasta dish, marrying tender protein with velvety pasta perfection.",
           "English",
           "",
           [
               RecipeLabel("ANIMAL", LabelCategory.ANIMAL),
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
           ]),
    Recipe("Vegetarian Stir-Fry",
           "Pizza is a beloved and versatile dish originating from Italy, featuring a thin or thick crust topped with a savory tomato sauce, melted cheese, and a variety of flavorful ingredients such as pepperoni, vegetables, and herbs. Its irresistible combination of crispy crust, gooey cheese, and an array of toppings makes pizza a universally cherished comfort food enjoyed worldwide.",
           "Italian",
           "",
           [
               RecipeLabel("ANIMAL", LabelCategory.ANIMAL),
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("VEGETABLESHERBS",
                           LabelCategory.VEGETABLESHERBS),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
           ]),
    Recipe("Pizza",
           "Pizza is a beloved and versatile dish originating from Italy, featuring a thin or thick crust topped with a savory tomato sauce, melted cheese, and a variety of flavorful ingredients such as pepperoni, vegetables, and herbs. Its irresistible combination of crispy crust, gooey cheese, and an array of toppings makes pizza a universally cherished comfort food enjoyed worldwide.",
           "Italian",
           "",
           [
               RecipeLabel("ANIMAL", LabelCategory.ANIMAL),
               RecipeLabel("MEAT", LabelCategory.MEAT),
               RecipeLabel("VEGETABLESHERBS",
                           LabelCategory.VEGETABLESHERBS),
               RecipeLabel("STAMPLEFOOD", LabelCategory.STAMPLEFOOD),
           ]),



]
