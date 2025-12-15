import streamlit as st
from ui_components import display_header, navigate_to
from data_manager import get_user_profile

def render_main_menu():
    """Render the main menu page"""
    display_header(f"👋 Hello, {st.session_state.name}!", 
                   "What would you like to do today?")
    
    st.markdown("---")
    
    # Check if user has saved profile
    user_profile = get_user_profile(st.session_state.name)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**👤 User:** {st.session_state.name}")
    with col2:
        if user_profile:
            st.success(f"**🎯 Your Recommended Calories:** {st.session_state.recommended_calories} kcal/day ✓")
        else:
            st.warning(f"**🎯 Recommended Calories:** {st.session_state.recommended_calories} kcal/day (Default - Calculate yours!)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🧮 Calorie Calculator")
        if user_profile:
            st.markdown("Update your daily calorie needs based on changes in your lifestyle")
        else:
            st.markdown("Calculate your daily calorie needs based on your personal information")
        if st.button("Open Calculator"):
            navigate_to('calculator')
    
    with col2:
        st.markdown("### 🍽️ Daily Meal Track")
        st.markdown("Log and track your meals throughout the day")
        if st.button("Track Meals"):
            navigate_to('meals')
    
    with col3:
        st.markdown("### 📊 History")
        st.markdown("View your daily calorie intake history and progress")
        if st.button("View History"):
            navigate_to('history')