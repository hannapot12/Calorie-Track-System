import json
import os
from datetime import datetime

# JSON file path
DATA_FILE = "calorie_data.json"

def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"meals": [], "users": {}}

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def save_user_profile(name, recommended_calories):
    """Save user profile with recommended calories"""
    data = load_data()
    if "users" not in data:
        data["users"] = {}
    data["users"][name] = {
        "recommended_calories": recommended_calories,
        "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_data(data)

def get_user_profile(name):
    """Get user profile"""
    data = load_data()
    if "users" in data and name in data["users"]:
        return data["users"][name]
    return None

def add_meal(user_name, meal_name, calories):
    """Add a new meal to JSON with user association"""
    data = load_data()
    meal = {
        "id": len(data["meals"]) + 1,
        "user_name": user_name,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "meal_name": meal_name,
        "calories": calories
    }
    data["meals"].append(meal)
    save_data(data)

def get_meals(user_name):
    """Get all meals for specified user only"""
    data = load_data()
    user_meals = [m for m in data["meals"] if m.get("user_name") == user_name]
    return [(m["id"], m["date"], m["meal_name"], m["calories"]) for m in user_meals]

def delete_meal(meal_id):
    """Delete a meal from JSON"""
    data = load_data()
    data["meals"] = [m for m in data["meals"] if m["id"] != meal_id]
    save_data(data)

def update_meal(meal_id, meal_name, calories):
    """Update a meal in JSON"""
    data = load_data()
    for meal in data["meals"]:
        if meal["id"] == meal_id:
            meal["meal_name"] = meal_name
            meal["calories"] = calories
            break
    save_data(data)