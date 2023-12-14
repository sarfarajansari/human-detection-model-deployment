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
    st.subheader('Architecture')
    Architecture = """
    The architecture of YOLO consists of a convolutional neural network i.e CNN which is inspired by GoogleNet 
    and is composed of several convolutional layers followed by fully connected layers: This means that the YOLO 
    architecture is made up of two types of layers - convolutional and fully connected layers. Convolutional
    layers are used to extract features from the input image, while fully connected layers are used to predict the
    class probabilities and bounding boxes for each object detected in the image.YOLO also uses various other techniques
    like anchor boxes, class prediction objectness score etc.., Which makes it efficient and accurate object detection
    algorithm that can process images in real-time, making it well-suited for applications such as self-driving cars,
    surveillance systems, and robotics.

    """
    st.text(Architecture)
    st.image('architecture.jpg')
    st.subheader('Training')
    Training = """
    The YOLOv8 model used in the AI Road Inspection System is trained on a large dataset of road images which were
    annotated with bounding boxes and class labels on Roboflow.Roboflow offers a range of datasets and annotation 
    tools specifically designed for computer vision and also provides a user-friendly interface and annotation 
    capabilities that stremline the process of labeling and preparing datasets for training machine learning models. 
    The training data includes diverse road conditions, different types of objects, and various environmental factors
    to ensure the model's generalization capability.
    
    """
    st.text(Training)
    st.subheader("Conclusion")
    conclusion = """
    The model is hence a cutting -edge solution that offers significant advancements over traditional manual inspection methods. 
    With its real time capabilities, the Ai Road Inspection System provides timely and accurate identification of road anomalies 
    such as potholes , cracks and alligator crakcs.This enables road maintenance teams to prioritize repairs efficiently, leading
    to improved road safety and optimized maintenance operations. 

    """
    st.markdown(conclusion, unsafe_allow_html=True)
