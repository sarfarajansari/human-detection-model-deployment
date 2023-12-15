import streamlit as st


def main():
    st.subheader('Introduction')
    Introduction = """
    The Ai road Inspection system , is an innovatiove solution that leverages computer vision and deep learning techniques
    to improve the road inspection and analysis. Traditional road Inspection methods often rely on manual labour 
    which is time consuming  and prone to human error. The AI road inspection system aims to address these limitations by enabling 
    real time detection, classification and analysis of various objects and anomalies on roads including potholes, cracks and 
    alligator cracks. 
    """
    st.text(Introduction)
