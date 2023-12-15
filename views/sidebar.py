import streamlit as st
import streamlit_option_menu as option_menu

def main():
    with st.sidebar:
        selected = option_menu.option_menu(
            "Main Menu",
            options=[
                "Model Information",
                "Predict"
                
            ],
        )


    st.sidebar.markdown('---')

    

    return selected