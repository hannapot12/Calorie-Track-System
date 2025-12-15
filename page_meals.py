import streamlit as st
from datetime import datetime
from ui_components import display_back_button
from calorie_calculator import get_food_database, calculate_item_calories
from data_manager import add_meal, get_meals, delete_meal

def render_meal_calculator():
    """Render the meal calorie calculator section"""
    st.markdown("## 🍴 Meal Calorie Calculator")
    st.markdown("Calculate calories for common meals and ingredients")
    
    food_database = get_food_database()
    
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        selected_food = st.selectbox(
            "Select Food Item",
            options=sorted(food_database.keys()),
            key="food_selector"
        )
    
    with col2:
        if any(keyword in selected_food for keyword in ["1 serving", "1 piece", "1 tbsp", "1 tsp", "1 cup", "1 slice", "1 large"]):
            quantity = st.number_input("Quantity (pieces/servings)", min_value=0.0, value=1.0, step=0.5)
            unit = "piece(s)"
        else:
            quantity = st.number_input("Quantity (grams)", min_value=0.0, value=100.0, step=10.0)
            unit = "g"
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Add Item", key="add_food_item"):
            item_calories = calculate_item_calories(selected_food, quantity)
            
            st.session_state.meal_items.append({
                "food": selected_food,
                "quantity": quantity,
                "unit": unit,
                "calories": round(item_calories, 1)
            })
            st.rerun()
    
    # Display added items
    if st.session_state.meal_items:
        st.markdown("---")
        st.markdown("#### 📋 Your Meal Items")
        
        total_meal_calories = 0
        
        for idx, item in enumerate(st.session_state.meal_items):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            
            with col1:
                st.write(f"**{item['food']}**")
            with col2:
                st.write(f"{item['quantity']} {item['unit']}")
            with col3:
                st.write(f"**{item['calories']} kcal**")
            with col4:
                if st.button("🗑️", key=f"remove_{idx}"):
                    st.session_state.meal_items.pop(idx)
                    st.rerun()
            
            total_meal_calories += item['calories']
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### 🔢 Total Meal Calories: **{round(total_meal_calories, 1)} kcal**")
        with col2:
            if st.button("🗑️ Clear All Items"):
                st.session_state.meal_items = []
                st.rerun()
        
        st.markdown("---")
        
        # Option to save this meal
        st.markdown("#### 💾 Save This Calculated Meal")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            meal_name_from_calc = st.text_input(
                "Meal Name",
                placeholder="e.g., Breakfast, Lunch, Dinner...",
                key="meal_name_from_calc"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("💾 Save to Tracker"):
                if meal_name_from_calc.strip():
                    add_meal(st.session_state.name, meal_name_from_calc.strip(), round(total_meal_calories, 1))
                    st.success(f"✅ Saved: {meal_name_from_calc} ({round(total_meal_calories, 1)} kcal)")
                    st.session_state.meal_items = []
                    st.rerun()
                else:
                    st.error("Please enter a meal name!")
    else:
        st.info("👆 Add food items above to calculate your meal's total calories")

def render_manual_entry():
    """Render manual meal entry section"""
    st.markdown("## ➕ Or Add Meal Manually")
    st.markdown("If you already know the calories, add your meal directly")
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        meal_name = st.text_input("Meal Name", placeholder="e.g., Breakfast, Chicken Salad...", key="manual_meal_name")
    with col2:
        calories = st.number_input("Calories (kcal)", min_value=0.0, step=1.0, key="manual_calories")
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Add Meal"):
            if meal_name.strip():
                add_meal(st.session_state.name, meal_name.strip(), calories)
                st.success(f"✅ Added: {meal_name} ({calories} kcal)")
                st.rerun()
            else:
                st.error("Please enter a meal name!")

def render_today_summary():
    """Render today's meal summary"""
    meals = get_meals(st.session_state.name)
    
    if meals:
        today = datetime.now().strftime("%Y-%m-%d")
        today_meals = [m for m in meals if m[1] == today]
        
        if today_meals:
            today_total = sum(m[3] for m in today_meals)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Calories Today", f"{today_total} kcal")
            with col2:
                st.metric("Recommended", f"{st.session_state.recommended_calories} kcal")
            with col3:
                diff = today_total - st.session_state.recommended_calories
                st.metric("Difference", f"{diff:+.0f} kcal")
            
            progress = min(today_total / st.session_state.recommended_calories, 1.5)
            st.progress(progress if progress <= 1 else 1.0)
            
            if today_total < st.session_state.recommended_calories:
                st.info(f"💡 You need {st.session_state.recommended_calories - today_total:.0f} more calories to reach your goal.")
            elif today_total > st.session_state.recommended_calories:
                st.warning(f"⚠️ You've exceeded your daily goal by {today_total - st.session_state.recommended_calories:.0f} calories.")
            else:
                st.success("✅ Perfect! You've reached your daily calorie goal!")
            
            st.markdown("---")
            st.markdown("#### Meal List")
            for meal in today_meals:
                col1, col2, col3 = st.columns([4, 1, 1])
                with col1:
                    st.write(f"**{meal[2]}**")
                    st.caption(f"Added: {meal[1]}")
                with col2:
                    st.write(f"**{meal[3]} kcal**")
                with col3:
                    if st.button("🗑️ Delete", key=f"del_{meal[0]}"):
                        delete_meal(meal[0])
                        st.rerun()
                st.markdown("---")
        else:
            st.info("📝 No meals logged today. Start tracking your meals above!")
    else:
        st.info("📝 No meals logged yet. Add your first meal above!")

def render_meals_page():
    """Render the daily meal tracking page"""
    display_back_button()
    
    st.title("🍽️ Daily Meal Track")
    st.markdown("Log your meals and track your daily calorie intake")
    st.markdown("---")
    
    # Meal Calculator
    render_meal_calculator()
    
    st.markdown("---")
    st.markdown("---")
    
    # Manual Entry
    render_manual_entry()
    
    st.markdown("---")
    
    # Today's Summary
    render_today_summary()