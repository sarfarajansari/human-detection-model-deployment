import streamlit as st


def main():
    st.subheader("Problem Statement")
    problem_statement = """
    Current practices of performing road inspections are time-consuming and labour-intensive. Road surfaces degrade on a 
    daily basis as a result of the heavy traffic on them.This will not only impact the driver’s comfort but will also
    impact economic efficiency. To maintain roads as efficiently as possible, municipalities perform regular
    inspections. The aim of the project is to use machine learning to study and analyze different types of road defects
    and to automatically detect any road abnormalities.
    
    The goal of this project is to design, build and test an inspection system for detecting road abnormalities, defects, and damages
    using machine learning. The proposed system aims to improve the efficiency of road inspections and reduce
    the time and labor required for the process. The system will be equipped with a camera to capture video streams
    from different roads, and the data will be analyzed using the Matlab machine learning toolbox to train and test the network.
    The output of the system will be recommended actions for the municipality to fix/correct any identified road defects. 
    The approach will involve three main tasks: data acquisition, data training/testing, and dashboard building and testing. 
    Ultimately, the proposed system will help to maintain roads more efficiently, enhance driver comfort, and improve economic 
    efficiency. Additionally, the system will provide insights into the causes of road abnormalities in Indian roads, 
    including pitfalls, sinks, flooding, and traffic congestion due to insufficient lanes in cities and towns.
    """

    st.text(problem_statement)
    st.subheader("Our Solution")
    Project_goal = """
    Our Team developed a Machine Learning ( ML ) model based on the YOLOv8 Architecture, which was trained on a comprehensive
    dataset of road images and manuallyannotated them to highlight the various types of road defects. Once the model was trained,
    we proceeded to test its performance on new and unseen data. This testing phase was vital to ensure that our model could
    generalize well and accurately identify road defects in real-world scenarios.In addition to the model,
    we developed a web application using the Streamlit API which serves as a user friendly interface for others to test the 
    trained model on their own videos and images
    """
    st.text(Project_goal)
