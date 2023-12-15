import streamlit as st
from views import model_information,  header, sidebar
from predict import predict


def main():
    with open("styles.css", "r") as source_style:
        st.markdown(f"<style>{source_style.read()}</style>",
                    unsafe_allow_html=True)
    header.main()
    selected = sidebar.main()

    if selected == "Predict":
        # Image
        upload_img_file = st.sidebar.file_uploader(
            'Upload Image', type=['jpg', 'jpeg', 'png'])
        if upload_img_file is not None:
            image_bytes = predict(upload_img_file)
            st.image(image_bytes, caption='Predicted Image',
                     use_column_width=True)

    elif selected == "Model Information":
        model_information.main()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
