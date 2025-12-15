import streamlit as st

# Import modules
from ui_components import apply_custom_css, initialize_session_state
from page_home import render_home_page
from page_menu import render_main_menu
from page_calculator import render_calculator_page
from page_meals import render_meals_page
from page_history import render_history_page

# Page configuration
st.set_page_config(
    page_title="CalorieTrack System", 
    page_icon="🍽️", 
    layout="wide"
)

# Initialize session state
initialize_session_state()

# Apply custom CSS
apply_custom_css()

# Page routing
def main():
    """Main application router"""
    
    if st.session_state.current_page == 'home':
        render_home_page()
    
    elif st.session_state.current_page == 'main_menu':
        render_main_menu()
    
    elif st.session_state.current_page == 'calculator':
        render_calculator_page()
    
    elif st.session_state.current_page == 'meals':
        render_meals_page()
    
    elif st.session_state.current_page == 'history':
        render_history_page()

# Run the application
if __name__ == "__main__":
    main()