import streamlit as st
from ui_components import navigate_to
from data_manager import get_user_profile

def render_home_page():
    """Render the home/welcome page"""
    st.markdown("""
        <style>
        .stApp {
            background-color: #BBD58E;
        }
        .big-font {
            font-weight: bold;
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(135deg, #45722D 5%, #6BA741 100%);
            color: white;
            border: none;
            padding: 15px;
            font-size: 16px;
            border-radius: 10px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        st.markdown('<p style="text-align: center; font-family: Georgia, serif; font-size: 48px; font-weight: bold; color: #344E41;">🍽️ CalorieTrack System</p>', unsafe_allow_html=True)
        
        st.markdown('<p style="text-align: center; font-family: Arial, sans-serif; font-size: 22px; color: #555555;">Welcome! Track your daily calorie intake with ease</p>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown('<p style="font-family: Verdana, sans-serif; font-size: 20px; font-weight: bold;">Please enter your name to get started:</p>', unsafe_allow_html=True)
        
        name = st.text_input("", label_visibility="collapsed", placeholder="Enter your name here...")
        
        if st.button("Next →"):
            if name.strip():
                st.session_state.name = name.strip()
                
                # Check if user already exists
                user_profile = get_user_profile(name.strip())
                if user_profile:
                    st.session_state.recommended_calories = user_profile["recommended_calories"]
                    st.success(f"Welcome back, {name.strip()}! 👋")
                    st.info(f"Your saved recommended calories: {user_profile['recommended_calories']} kcal/day")
                else:
                    st.info("New user detected! You can calculate your recommended calories in the main menu.")
                
                navigate_to('main_menu')
            else:
                st.error("Please enter your name!")

        st.markdown(
            """
            <p style="text-align: center; font-family: Verdana, sans-serif; 
               font-size: 13px; color: #3A3A3A; margin-top: 20px;">
               This system helps you understand and manage your daily nutrition 
               in a simple and meaningful way. It supports <b>SDG 3: Good Health and Well-Being</b> by encouraging 
               a healthier lifestyle for everyone.
            </p>
            """,
            unsafe_allow_html=True
        )