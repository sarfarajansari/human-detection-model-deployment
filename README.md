

# Human Detection Model Deployment

This repository contains the deployment setup for a human detection model built by the AI club in my college. My role in this project was to to deploy the model with a user-friendly Streamlit interface for easy interaction.






https://github.com/user-attachments/assets/dacc8fbe-96cc-4757-afee-e14c8d9a8064




## Overview

The human detection model is designed to detect human figures within images or video streams. The AI club developed the core model as part of Omdena project, and I was tasked with handling the deployment process to make the model accessible through a simple web interface using Streamlit.

## Key Responsibilities

- **Package Version Management**: Ensuring all dependencies were correctly handled using `requirements.txt` to avoid compatibility issues between different packages and environments.
- **Model Deployment**: Deploying the human detection model using Streamlit, creating a simple UI that allows users to upload images and view the detection results.
- **UI Implementation**: Creating a clean and intuitive interface with Streamlit that allows easy interaction with the model, including image upload and result visualization.

## Features

- **Image Upload**: Users can upload an image via the UI for human detection.
- **Real-Time Detection**: Once the image is uploaded, the model processes the image and highlights detected humans.
- **Streamlit Interface**: A lightweight and interactive web interface built using Streamlit, allowing for easy integration with machine learning models.
- **Simple and Intuitive UI**: The UI is designed to be user-friendly, making it easy for non-technical users to interact with the model.

## Technologies Used

- **Streamlit**: Used to create the interactive web interface for model deployment.
- **Python**: The primary programming language for managing model deployment and handling backend logic.
- **Machine Learning Model**: Built by the AI club, this model uses deep learning techniques to detect humans in images.



## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/sarfarajansari/human-detection-model-deployment.git
   ```



2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.


