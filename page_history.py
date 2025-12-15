import streamlit as st
import pandas as pd
from ui_components import display_back_button, color_remark
from calorie_calculator import get_remark
from data_manager import get_meals, update_meal, delete_meal

def render_daily_summary_tab():
    """Render the daily summary tab"""
    st.markdown(f"### 📅 {st.session_state.name}'s Daily Summary")
    
    meals = get_meals(st.session_state.name)
    
    daily_summary = {}
    for row in meals:
        date, meal, cal = row[1], row[2], row[3]
        daily_summary.setdefault(date, 0)
        daily_summary[date] += cal
    
    daily_data = []
    for date, total in sorted(daily_summary.items(), reverse=True):
        remark = get_remark(total, st.session_state.recommended_calories)
        daily_data.append({
            "Date": date,
            "Total Calories": f"{total} kcal",
            "Recommended": f"{st.session_state.recommended_calories} kcal",
            "Difference": f"{total - st.session_state.recommended_calories:+.0f} kcal",
            "Remark": remark
        })
    
    df_daily = pd.DataFrame(daily_data)
    styled_df = df_daily.style.applymap(color_remark, subset=['Remark'])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown(f"### 📈 {st.session_state.name}'s Overall Statistics")
    
    total_days = len(daily_summary)
    average_calories = sum(daily_summary.values()) / total_days
    insufficient_days = sum(1 for total in daily_summary.values() if total < st.session_state.recommended_calories)
    sufficient_days = sum(1 for total in daily_summary.values() if total == st.session_state.recommended_calories)
    excess_days = sum(1 for total in daily_summary.values() if total > st.session_state.recommended_calories)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Days Logged", total_days)
    with col2:
        st.metric("Average Daily Intake", f"{average_calories:.0f} kcal")
    with col3:
        st.metric("Insufficient Days", insufficient_days)
    with col4:
        st.metric("Excess Days", excess_days)

def render_update_meals_tab():
    """Render the update meals tab"""
    st.markdown(f"### ✏️ Update {st.session_state.name}'s Meal Records")
    st.markdown("Select a meal to update its details")
    
    meals = get_meals(st.session_state.name)
    
    meals_by_date = {}
    for meal in meals:
        date = meal[1]
        meals_by_date.setdefault(date, [])
        meals_by_date[date].append(meal)
    
    selected_date = st.selectbox(
        "Select Date",
        options=sorted(meals_by_date.keys(), reverse=True),
        format_func=lambda x: f"{x} ({len(meals_by_date[x])} meals)"
    )
    
    if selected_date:
        st.markdown("---")
        date_meals = meals_by_date[selected_date]
        
        st.markdown(f"#### Meals on {selected_date}")
        
        for meal in date_meals:
            meal_id, date, meal_name, meal_calories = meal
            
            with st.expander(f"🍽️ {meal_name} - {meal_calories} kcal"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    new_meal_name = st.text_input(
                        "Meal Name",
                        value=meal_name,
                        key=f"name_{meal_id}"
                    )
                    new_calories = st.number_input(
                        "Calories (kcal)",
                        value=float(meal_calories),
                        min_value=0.0,
                        step=1.0,
                        key=f"cal_{meal_id}"
                    )
                
                with col2:
                    st.markdown("<br>", unsafe_allow_html=True)
                    col_update, col_delete = st.columns(2)
                    
                    with col_update:
                        if st.button("💾 Update", key=f"update_{meal_id}"):
                            if new_meal_name.strip():
                                update_meal(meal_id, new_meal_name.strip(), new_calories)
                                st.success(f"✅ Updated: {new_meal_name}")
                                st.rerun()
                            else:
                                st.error("Meal name cannot be empty!")
                    
                    with col_delete:
                        if st.button("🗑️ Delete", key=f"delete_{meal_id}"):
                            delete_meal(meal_id)
                            st.success(f"🗑️ Deleted meal")
                            st.rerun()
                
                st.caption(f"Added on: {date}")
        
        st.markdown("---")
        daily_total = sum(m[3] for m in date_meals)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total for this day", f"{daily_total} kcal")
        with col2:
            st.metric("Recommended", f"{st.session_state.recommended_calories} kcal")
        with col3:
            diff = daily_total - st.session_state.recommended_calories
            st.metric("Difference", f"{diff:+.0f} kcal")

def render_history_page():
    """Render the history page"""
    display_back_button()
    
    st.title("📊 History")
    st.markdown(f"View and manage **{st.session_state.name}'s** daily calorie intake history")
    st.markdown("---")
    
    meals = get_meals(st.session_state.name)
    
    if meals:
        tab1, tab2 = st.tabs(["📅 Daily Summary", "✏️ Update Meals"])
        
        with tab1:
            render_daily_summary_tab()
        
        with tab2:
            render_update_meals_tab()
    else:
        st.info(f"📝 No history available yet for {st.session_state.name}. Start tracking your meals!")