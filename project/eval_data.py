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
        title="Coq au Vin",
        description="Coq au Vin is a classic French dish that features chicken cooked in red wine, mushrooms, and bacon. It is known for its rich and flavorful sauce, often served with potatoes or crusty bread.",
        origin="French"
    ),
    Recipe(
        title="Ratatouille",
        description="Ratatouille is a traditional Provençal vegetable stew that typically includes ingredients like eggplant, zucchini, bell peppers, onions, and tomatoes. It is seasoned with herbs and often served as a side dish or main course.",
        origin="French"
    ),
    Recipe(
        title="Bouillabaisse",
        description="Bouillabaisse is a traditional fisherman's stew originating from the port city of Marseille. It features a variety of fish, shellfish, and aromatic herbs in a broth flavored with spices like saffron and served with rouille sauce.",
        origin="French"
    ),
    Recipe(
        title="Quiche Lorraine",
        description="Quiche Lorraine is a savory tart originating from the Lorraine region. It consists of a pastry crust filled with a custard mixture of eggs, cream, and bacon. While variations may include other ingredients, the classic version remains a popular choice.",
        origin="French"
    ),
    Recipe(
        title="Cassoulet",
        description="Cassoulet is a hearty, slow-cooked casserole originating from the region of Languedoc. It typically includes white beans, various meats such as sausage, pork, and duck confit, all baked together for a savory and satisfying dish.",
        origin="French"
    ),
    Recipe(
        title="Pizza",
        description="Pizza is a beloved and versatile dish originating from Italy, featuring a thin or thick crust topped with a savory tomato sauce, melted cheese, and a variety of flavorful ingredients such as pepperoni, vegetables, and herbs. Its irresistible combination of crispy crust, gooey cheese, and an array of toppings makes pizza a universally cherished comfort food enjoyed worldwide.",
        origin="Italian"
    ),
    Recipe(
        title="Margherita Pizza",
        description="Margherita Pizza is a simple and iconic Italian pizza topped with tomato sauce, fresh mozzarella cheese, basil leaves, and a drizzle of olive oil. It is named after Queen Margherita of Italy and represents the colors of the Italian flag.",
        origin="Italian"
    ),
    Recipe(
        title="Risotto",
        description="Risotto is a creamy Italian rice dish made by cooking rice slowly in broth until it reaches a creamy consistency. There are various types of risotto, and popular variations include Risotto alla Milanese (saffron-infused), Risotto ai Funghi (with mushrooms), and Risotto al Nero di Seppia (with cuttlefish ink).",
        origin="Italian"
    ),
    Recipe(
        title="Osso Buco",
        description="Osso Buco is a traditional Milanese dish that consists of braised veal shanks cooked with white wine, broth, onions, carrots, celery, and tomatoes. The marrow inside the veal bones adds richness to the dish. It is often served with a gremolata—a mixture of lemon zest, garlic, and parsley.",
        origin="Italian"
    ),
    Recipe(
        title="Spaghetti Bolognese",
        description="A comforting Italian classic, spaghetti Bolognese features al dente pasta smothered in a rich, slow-cooked tomato and meat sauce, creating a hearty and satisfying meal.",
        origin="Italian"
    ),
    Recipe(
        title="Vegetarian Stir-Fry",
        description="A comforting Italian classic, spaghetti Bolognese features al dente pasta smothered in a rich, slow-cooked tomato and meat sauce, creating a hearty and satisfying meal.",
        origin="Italian"
    ),
    Recipe(
        title="Chicken Alfredo",
        description="Succulent grilled chicken meets creamy Alfredo sauce in this indulgent pasta dish, marrying tender protein with velvety pasta perfection.",
        origin="English"
    ),
    Recipe(
        title="Mashed potato",
        description="Creamy and comforting, mashed potatoes are a staple in American cuisine, often gracing tables during holiday feasts and everyday meals alike. Potatoes are boiled, mashed, and whipped with butter and milk, creating a velvety side dish that perfectly complements a variety of main courses, showcasing the timeless appeal of this classic comfort food in the United States and beyond.",
        origin="English"
    ),
    Recipe(
        title="Poutine",
        description="Poutine, a Canadian culinary delight, consists of crispy French fries topped with fresh cheese curds and drenched in savory brown gravy. This irresistible combination of textures and flavors creates a comforting and indulgent dish that has become a symbol of Canadian cuisine.",
        origin="English"
    ),
    Recipe(
        title="Roast Beef and Yorkshire Pudding",
        description="Roast Beef and Yorkshire Pudding is a traditional Sunday roast in British cuisine. It features roast beef served with Yorkshire puddings, which are light, crispy, and fluffy batter puddings. The dish is often accompanied by roasted vegetables and gravy.",
        origin="English"
    ),
    Recipe(
        title="Fish and Chips",
        description="Fish and Chips is a classic British dish that consists of battered and deep-fried fish (usually cod or haddock) served with thick-cut potatoes, often as chips (fries). It is commonly accompanied by condiments like tartar sauce, mushy peas, or vinegar.",
        origin="English"
    ),
    Recipe(
        title="Crumble",
        description="Crumble, a classic dessert, showcases a delectable mix of sweet, spiced fruit filling topped with a crumbly mixture of flour, butter, and sugar. Baked to golden perfection, this comforting dish, often made with apples, berries, or stone fruits, delivers a delightful contrast between the warm, gooey interior and the crisp, buttery crumb topping, making it a beloved treat in British and American kitchens alike.",
        origin="English"
    ),
    Recipe(
        title="Wonton",
        description="Wontons are delicate Chinese dumplings, typically made by wrapping seasoned minced meat, such as pork or shrimp, in thin sheets of dough. These little parcels are then boiled, steamed, or fried, resulting in bite-sized pockets of savory goodness enjoyed in soups or as appetizers, showcasing the artful simplicity of Chinese culinary craftsmanship.",
        origin="Chinese"
    ),
    Recipe(
        title="Peking Duck",
        description="Peking Duck is a famous Chinese dish that originated in Beijing. It features thin, crispy slices of roast duck served with thin pancakes, hoisin sauce, and sliced scallions. The dish is known for its crispy skin and flavorful meat.",
        origin="Chinese"
    ),
    Recipe(
        title="Dim Sum",
        description="Dim Sum refers to a variety of bite-sized Chinese dishes traditionally served in small steamer baskets or on small plates. Dim Sum includes a wide range of items such as dumplings, buns, rolls, and desserts, often served in a brunch or lunch setting.",
        origin="Chinese"
    ),
    Recipe(
        title="Mapo Tofu",
        description="Mapo Tofu is a spicy and flavorful Sichuan dish made with tofu, minced meat (usually pork or beef), and a spicy chili and bean-based sauce. It is known for its bold flavors and numbing sensation from Sichuan peppercorns.",
        origin="Chinese"
    ),
    Recipe(
        title="Kung Pao Chicken",
        description="Kung Pao Chicken is a spicy and savory Chinese stir-fry dish that typically includes diced chicken, peanuts, vegetables, and chili peppers. It is known for its bold flavors and is named after Ding Baozhen, a Qing Dynasty official with the title Kung Pao.",
        origin="Chinese"
    ),
    Recipe(
        title="Hot Pot (火锅)",
        description="Hot Pot is a popular Chinese cooking method where ingredients, such as thinly sliced meat, vegetables, and noodles, are cooked in a simmering pot of broth at the dining table. The broth can be spicy or non-spicy, and various dipping sauces complement the cooked ingredients.",
        origin="Chinese"
    ),
    Recipe(
        title="Taco",
        description="Tacos are a Mexican culinary treasure, featuring a folded or rolled tortilla filled with a variety of savory ingredients such as seasoned meats, beans, lettuce, cheese, and salsa. The diverse combination of flavors and textures in each taco, often accompanied by a squeeze of lime, offers a handheld delight that has become a global favorite, celebrated for its versatility and delicious simplicity.",
        origin="Mexican"
    ),
    Recipe(
        title="Ceviche",
        description="Ceviche is a refreshing and tangy seafood dish made with raw fish or seafood marinated in citrus juices, typically lime or lemon juice. The acidity from the citrus 'cooks' the seafood, and it is often mixed with tomatoes, onions, cilantro, and chili peppers.",
        origin="Mexican"
    ),
    Recipe(
        title="Guacamole",
        description="Guacamole is a popular Mexican dip made from mashed avocados, lime juice, tomatoes, onions, and cilantro. It is often seasoned with salt and pepper and served with tortilla chips or as a condiment for various dishes.",
        origin="Mexican"
    ),
    Recipe(
        title="Enchiladas",
        description="Enchiladas are rolled tortillas filled with various ingredients, such as meat, cheese, beans, or vegetables, and topped with chili sauce. The dish is typically baked until the tortillas are heated through, and the flavors meld together.",
        origin="Mexican"
    ),
    Recipe(
        title="Mole",
        description="Mole is a rich and flavorful sauce in Mexican cuisine, made from a combination of chili peppers, chocolate, spices, and other ingredients. There are various types of mole, each with its unique flavor profile, and it is often served with meats such as chicken or turkey.",
        origin="Mexican"
    ),
    Recipe(
        title="Chiles Rellenos",
        description="Chiles Rellenos are large, mild chili peppers stuffed with cheese or meat, dipped in egg batter, and fried until golden. They are often served with tomato sauce or salsa and can be accompanied by rice and beans.",
        origin="Mexican"
    ),
    Recipe(
        title="Pierogi",
        description="Pierogi, a beloved Eastern European dish, hails from Poland and holds a special place in its culinary tradition. These dumplings are filled with a delectable mixture of ingredients like potatoes, cheese, meat, or sauerkraut. Typically boiled or fried, pierogi are enjoyed throughout the region, with variations found in countries such as Ukraine and Russia. Served with toppings like sour cream, onions, or butter, pierogi offer a satisfying and versatile comfort food experience.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Pierogi",
        description="Pierogi, a beloved Eastern European dish, hails from Poland and holds a special place in its culinary tradition. These dumplings are filled with a delectable mixture of ingredients like potatoes, cheese, meat, or sauerkraut. Typically boiled or fried, pierogi are enjoyed throughout the region, with variations found in countries such as Ukraine and Russia. Served with toppings like sour cream, onions, or butter, pierogi offer a satisfying and versatile comfort food experience.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Borscht (Борщ)",
        description="Borscht is a traditional Ukrainian beetroot soup that can be served hot or cold. It typically includes beets, cabbage, potatoes, carrots, onions, and sometimes meat, creating a vibrant and hearty dish.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Varenyky (Вареники)",
        description="Varenyky are Ukrainian dumplings typically filled with potatoes, cheese, cabbage, meat, or fruit. They are boiled and then served with sour cream, butter, or fried onions.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Holubtsi",
        description="Holubtsi are Ukrainian cabbage rolls filled with a mixture of rice and minced meat, often pork or beef. The rolls are then baked or stewed in a tomato-based sauce.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Deruny",
        description="Deruny are Ukrainian potato pancakes made from grated potatoes mixed with flour, eggs, and onions. They are fried until golden brown and can be served with sour cream or applesauce.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Kutia ",
        description="Kutia is a traditional Ukrainian dish often served during the Christmas season. It is a sweet wheat berry pudding made with poppy seeds, honey, nuts, and dried fruits.",
        origin="Ukrainian"
    ),
    Recipe(
        title="Roti canai",
        description="Roti canai is a popular Malaysian and Indian dish, featuring thin, flaky, and stretchy flatbread that is skillfully prepared by tossing and flipping the dough. Served with flavorful curries or dhal, this versatile and delicious flatbread has become a breakfast favorite and street food staple, symbolizing the rich culinary heritage of Malaysia and its South Asian influences.",
        origin="Malay"
    ),
    Recipe(
        title="Nasi Lemak",
        description="Nasi Lemak is a national dish of Malaysia, consisting of fragrant rice cooked in coconut milk and pandan leaves. It is typically served with anchovies, peanuts, boiled eggs, cucumber, and sambal (spicy chili paste).",
        origin="Malay"
    ),
    Recipe(
        title="Satay",
        description="Satay is a popular Malaysian dish featuring skewered and grilled meat, often served with a flavorful peanut sauce. The skewers can be made with various meats, such as chicken, beef, or lamb.",
        origin="Malay"
    ),
    Recipe(
        title="Laksa",
        description="Laksa is a spicy noodle soup that comes in various regional variations across Malaysia. It typically includes rice noodles, spicy broth made with coconut milk, seafood or chicken, bean sprouts, and herbs.",
        origin="Malay"
    ),
    Recipe(
        title="Roti Canai",
        description="Roti Canai is a type of Indian-influenced flatbread that is popular in Malaysia. It is often served with dhal (lentil curry) or curry sauce and can be enjoyed for breakfast or as a snack.",
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
        title="Paneer Tikka",
        description="Paneer Tikka is a popular Indian appetizer where marinated cubes of paneer (Indian cottage cheese) are skewered and grilled or baked. It is often served with mint chutney and is known for its smoky flavor.",
        origin="Hindi"
    ),
    Recipe(
        title="Biryani",
        description="Biryani is a flavorful and aromatic rice dish made with basmati rice, meat (such as chicken, mutton, or beef), and a blend of spices. It is often layered and cooked to perfection, creating a fragrant and richly spiced dish.",
        origin="Hindi"
    ),
    Recipe(
        title="Dal Makhani (दाल मखनी)",
        description="Dal Makhani is a creamy lentil dish made with black gram lentils, kidney beans, butter, and cream. It is slow-cooked to achieve a rich and indulgent flavor and is commonly enjoyed with rice or Indian bread.",
        origin="Hindi"
    ),

    Recipe(
        title="Knieperkohl",
        description="Knieperkohl is a traditional German dish, particularly popular in the region of Brandenburg. It consists of pickled cabbage, often combined with various vegetables and spices. This tangy and flavorful dish is typically enjoyed as a side dish or accompaniment, adding a distinctive taste to German meals and reflecting the country's rich culinary heritage.",
        origin="German"
    ),
    Recipe(
        title="Sauerbraten",
        description="Sauerbraten is a German pot roast, typically made with marinated and slow-cooked beef, often served with a sweet and sour gravy. The marinade includes ingredients such as vinegar, wine, and a variety of spices.",
        origin="German"
    ),

    Recipe(
        title="Bratwurst",
        description="Bratwurst is a type of German sausage made from pork, veal, or beef. It is seasoned with a blend of spices and herbs, then grilled or pan-fried. Bratwurst is often served with mustard and bread or in a roll.",
        origin="German"
    ),

    Recipe(
        title="Wiener Schnitzel:",
        description="Wiener Schnitzel is a classic Austrian and German dish consisting of breaded and deep-fried veal or pork cutlets. It is typically served with lemon wedges and may be accompanied by potato salad or potatoes.",
        origin="German"
    ),

    Recipe(
        title="Kartoffelsalat",
        description="Kartoffelsalat is a German potato salad that comes in various regional variations. It often includes boiled potatoes, onions, bacon, and a tangy dressing made with vinegar, oil, and mustard.",
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
