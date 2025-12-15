import math

def calculate_bmr(age, weight, height, gender, activity):
    """Calculate BMR using Mifflin-St Jeor Equation"""
    if gender.upper() == "M":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return math.ceil(bmr * activity)

def get_remark(total, recommended):
    """Get calorie intake remark"""
    if total < recommended:
        return "Insufficient"
    elif total == recommended:
        return "Sufficient"
    else:
        return "Excess"

# Food database with calories per 100g or per serving
FOOD_DATABASE = {
    # Filipino Dishes (per serving)
    "Adobo (1 serving)": 350,
    "Sinigang na Baboy (1 serving)": 280,
    "Sinigang na Hipon (1 serving)": 220,
    "Tinola (1 serving)": 200,
    "Kare-Kare (1 serving)": 450,
    "Lechon Kawali (1 serving)": 420,
    "Bicol Express (1 serving)": 380,
    "Sisig (1 serving)": 400,
    "Menudo (1 serving)": 320,
    "Caldereta (1 serving)": 380,
    "Mechado (1 serving)": 340,
    "Pinakbet (1 serving)": 180,
    "Ginataang Gulay (1 serving)": 250,
    "Lumpia Shanghai (1 piece)": 50,
    "Pancit Canton (1 serving)": 300,
    "Pancit Bihon (1 serving)": 280,
    "Chicken Inasal (1 serving)": 320,
    "Lechon (100g)": 450,
    "Longganisa (1 piece)": 180,
    "Tocino (100g)": 280,
    "Tuyo (1 piece)": 45,
    "Daing na Bangus (1 piece)": 200,
    "Tapa (100g)": 250,
    "Champorado (1 cup)": 220,
    "Lugaw (1 cup)": 140,
    "Arroz Caldo (1 cup)": 180,
    "Halo-Halo (1 cup)": 350,
    "Leche Flan (1 slice)": 180,
    "Bibingka (1 piece)": 200,
    "Puto (1 piece)": 90,
    "Kutsinta (1 piece)": 85,
    "Sapin-Sapin (1 piece)": 150,
    "Palabok (1 serving)": 400,
    # Student Budget Meals & Street Food
    "Siomai (1 piece)": 35,
    "Siomai Rice (1 serving)": 280,
    "Hotdog/Hatdog (1 piece)": 150,
    "Hotdog Sandwich": 320,
    "Fishball (1 piece)": 15,
    "Kikiam (1 piece)": 40,
    "Squidball (1 piece)": 18,
    "Chicken Ball (1 piece)": 25,
    "Kwek-kwek (1 piece)": 60,
    "Tokneneng (1 piece)": 80,
    "Isaw (1 stick)": 70,
    "Betamax (1 piece)": 45,
    "Adidas (1 piece)": 55,
    "Proven (1 piece)": 50,
    "Helmet (1 piece)": 60,
    "Calamares (1 serving)": 250,
    "Turon (1 piece)": 120,
    "Banana Cue (1 piece)": 150,
    "Kamote Cue (1 piece)": 130,
    "Maruya (1 piece)": 110,
    # Instant/Canned Foods
    "Instant Pancit Canton (1 pack)": 320,
    "Cup Noodles (1 cup)": 300,
    "Instant Ramen (1 pack)": 380,
    "Corned Beef (100g)": 220,
    "Corned Beef with Rice": 450,
    "Spam (1 slice)": 180,
    "Luncheon Meat (1 slice)": 160,
    "Vienna Sausage (1 piece)": 45,
    "Meatloaf (100g)": 200,
    "Sardines in Oil (100g)": 210,
    "Sardines in Tomato Sauce (100g)": 160,
    "Century Tuna (100g)": 130,
    "Liver Spread (1 tbsp)": 40,
    "Spam Sandwich": 380,
    # Fast Food Style
    "Burger (regular)": 250,
    "Cheeseburger": 300,
    "Fried Chicken (1 piece)": 320,
    "Chicken Nuggets (1 piece)": 50,
    "French Fries (regular)": 320,
    "Pizza Slice": 285,
    "Shawarma Rice": 450,
    "Shawarma Wrap": 400,
    # Snacks & Chips
    "Chippy (1 pack 110g)": 570,
    "Piattos (1 pack 85g)": 420,
    "Nova (1 pack 78g)": 410,
    "Cheese Ring (1 pack)": 380,
    "Skyflakes (1 piece)": 30,
    "Bread Pan/Pandesal (1 piece)": 120,
    "Ensaymada (1 piece)": 280,
    "Monay (1 piece)": 180,
    "Spanish Bread (1 piece)": 150,
    "Cheese Bread (1 piece)": 200,
    # Drinks Common for Students
    "3-in-1 Coffee (1 sachet)": 70,
    "Milo Drink (1 sachet)": 90,
    "Softdrinks (1 can 330ml)": 140,
    "Iced Tea (1 bottle)": 120,
    "Milk Tea (regular)": 300,
    "Fruit Juice (1 box)": 110,
    "Energy Drink (1 can)": 110,
    # Karinderya/Carinderia Favorites
    "Tortang Talong (1 piece)": 120,
    "Pork Chop (1 piece)": 280,
    "Fried Tilapia (1 piece)": 180,
    "Pritong Isda (1 piece)": 200,
    "Nilagang Baka (1 serving)": 300,
    "Bulalo (1 serving)": 350,
    "Goto (1 bowl)": 250,
    "Mami (1 bowl)": 300,
    "Lomi (1 bowl)": 380,
    "Batchoy (1 bowl)": 320,
    "Pares (1 serving)": 450,
    "Tapsilog (1 serving)": 550,
    "Tocilog (1 serving)": 520,
    "Longsilog (1 serving)": 580,
    "Bangsilog (1 serving)": 480,
    "Cornsilog (1 serving)": 600,
    "Spamsilog (1 serving)": 620,
    "Sisigsilog (1 serving)": 650,
    "Fried Egg (1 piece)": 90,
    "Scrambled Egg (1 serving)": 140,
    # Basic Ingredients
    "Rice (cooked, 1 cup)": 200,
    "Rice (cooked, per 100g)": 130,
    "Brown Rice (cooked)": 112,
    "Fried Rice (1 serving)": 350,
    "Garlic Rice (1 serving)": 280,
    "Chicken Breast (cooked)": 165,
    "Beef (cooked)": 250,
    "Pork (cooked)": 242,
    "Fish (cooked)": 206,
    "Egg (1 large)": 78,
    "Bread (1 slice)": 79,
    "Tasty Bread (1 loaf)": 110,
    "Wheat Bread (1 slice)": 70,
    "Pasta (cooked)": 131,
    "Potato (cooked)": 87,
    "Kamote/Sweet Potato": 86,
    "Cassava": 160,
    # Vegetables
    "Broccoli": 34,
    "Carrot": 41,
    "Tomato": 18,
    "Lettuce": 15,
    "Cucumber": 16,
    "Bell Pepper": 31,
    "Onion": 40,
    "Garlic": 149,
    "Sitaw/String Beans": 31,
    "Talong/Eggplant": 25,
    "Kangkong": 19,
    "Pechay": 13,
    "Ampalaya": 17,
    "Sayote": 19,
    "Malunggay": 64,
    # Fruits
    "Apple": 52,
    "Banana": 89,
    "Orange": 47,
    "Mango": 60,
    "Papaya": 43,
    "Pineapple": 50,
    "Watermelon": 30,
    "Calamansi (1 piece)": 3,
    # Protein
    "Salmon": 208,
    "Tuna": 132,
    "Shrimp": 99,
    "Tilapia": 128,
    "Bangus/Milkfish": 152,
    "Galunggong": 150,
    "Tofu": 76,
    # Dairy & Others
    "Milk (1 cup)": 149,
    "Cheese": 402,
    "Yogurt": 59,
    "Butter": 717,
    "Cooking Oil (1 tbsp)": 120,
    "Olive Oil (1 tbsp)": 119,
    "Coconut Oil (1 tbsp)": 117,
    "Soy Sauce (1 tbsp)": 8,
    "Fish Sauce/Patis (1 tbsp)": 6,
    "Vinegar (1 tbsp)": 3,
    "White Sugar (1 tsp)": 16,
    "Brown Sugar (1 tsp)": 15,
    "Peanut Butter (1 tbsp)": 94,
    "Avocado": 160,
    "Coconut Milk (1 cup)": 445,
    "Evaporated Milk (1 tbsp)": 21,
    "Condensed Milk (1 tbsp)": 61
}

def get_food_database():
    """Return the food database"""
    return FOOD_DATABASE

def calculate_item_calories(food_item, quantity):
    """Calculate calories for a food item based on quantity"""
    base_calories = FOOD_DATABASE[food_item]
    
    # Check if it's a per-piece/serving item
    if any(keyword in food_item for keyword in ["1 serving", "1 piece", "1 tbsp", "1 tsp", "1 cup", "1 slice", "1 large"]):
        return base_calories * quantity
    else:
        # Calculate per 100g
        return (base_calories / 100) * quantity