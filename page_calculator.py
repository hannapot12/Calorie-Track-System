import streamlit as st
from ui_components import display_back_button
from calorie_calculator import calculate_bmr
from data_manager import get_user_profile, save_user_profile

def render_calculator_page():
    """Render the calorie calculator page"""
    display_back_button()
    
    st.title("🧮 Calorie Calculator")
    
    # Check if user has existing profile
    user_profile = get_user_profile(st.session_state.name)
    if user_profile:
        st.info(f"📋 Your current recommended calories: **{user_profile['recommended_calories']} kcal/day**")
        st.markdown("You can recalculate if your weight, activity level, or other factors have changed.")
    else:
        st.markdown("Calculate your recommended daily calorie intake based on your personal information")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Personal Information")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
    
    with col2:
        st.markdown("#### Additional Details")
        gender = st.selectbox("Gender", ["M", "F"])
        activity = st.selectbox(
            "Activity Level",
            [
                ("Sedentary (little or no exercise)", 1.2),
                ("Lightly active (exercise 1-3 days/week)", 1.375),
                ("Moderately active (exercise 3-5 days/week)", 1.55),
                ("Very active (exercise 6-7 days/week)", 1.725),
                ("Extra active (very intense exercise)", 1.9)
            ],
            format_func=lambda x: x[0]
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Calculate Recommended Calories"):
        recommended = calculate_bmr(age, weight, height, gender, activity[1])
        st.session_state.recommended_calories = recommended
        
        # Save user profile
        save_user_profile(st.session_state.name, recommended)
        
        st.success("✅ Calculation Complete!")
        st.markdown(f"## Your recommended daily calories: **{recommended} kcal**")
        st.info("💾 Your recommended calories have been saved to your profile!")
        st.balloons()