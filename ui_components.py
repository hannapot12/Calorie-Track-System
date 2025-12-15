import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the app"""
    st.markdown("""
        <style>
        .stApp {
            background-color: #BBD583;
        }

        .big-font {
            font-size:24px !important;
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

def navigate_to(page):
    """Navigate to a different page"""
    st.session_state.current_page = page
    st.rerun()

def initialize_session_state():
    """Initialize all session state variables"""
    if 'name' not in st.session_state:
        st.session_state.name = None
    if 'recommended_calories' not in st.session_state:
        st.session_state.recommended_calories = 2000
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    if 'meal_items' not in st.session_state:
        st.session_state.meal_items = []

def display_header(title, subtitle=None):
    """Display a formatted header"""
    st.markdown(f'''
        <h1 style="color: 4E2A20; text-align: center; font-size: 50px;">
            {title}
        </h1>
    ''', unsafe_allow_html=True)
    
    if subtitle:
        st.markdown(f'''
            <h3 style="text-align: center; font-size: 28px;">
                {subtitle}
            </h3>
        ''', unsafe_allow_html=True)

def display_back_button():
    """Display a back to menu button"""
    if st.button("← Back to Menu"):
        navigate_to('main_menu')

def color_remark(val):
    """Return color styling based on remark value"""
    if val == 'Insufficient':
        return 'background-color: #fff3cd'
    elif val == 'Sufficient':
        return 'background-color: #d4edda'
    elif val == 'Excess':
        return 'background-color: #f8d7da'
    return ''