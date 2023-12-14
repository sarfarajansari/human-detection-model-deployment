import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io
import tempfile
import os
from views import project_information, model_information, contributers, header, sidebar


model = YOLO('best.pt')


def process_video(video_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps is None:
        fps = 30  # Set a default value for fps if it is 0 or None

    # Create a list to store the processed frames
    processed_frames = []

    # Process each frame in the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform the prediction on the frame
        prediction = model.predict(frame)
        frame_with_bbox = prediction[0].plot()

        # Convert the frame to PIL Image and store in the list
        processed_frames.append(Image.fromarray(frame_with_bbox))

    cap.release()

    # Create the output video file path
    video_path_output = "output.mp4"

    # Save the processed frames as individual images
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, frame in enumerate(processed_frames):
            frame.save(f"{temp_dir}/frame_{i}.png")

        # Create a video clip from the processed frames
        video_clip_path = f"{temp_dir}/clip.mp4"
        os.system(
            f"ffmpeg -framerate {fps} -i {temp_dir}/frame_%d.png -c:v libx264 -pix_fmt yuv420p {video_clip_path}")

        # Rename the video clip with the desired output path
        os.rename(video_clip_path, video_path_output)

    return video_path_output


def main():
    with open("styles.css", "r") as source_style:
        st.markdown(f"<style>{source_style.read()}</style>",
                    unsafe_allow_html=True)
    header.main()
    selected = sidebar.main()

    # HOME page

    if selected == "Project Information":
        project_information.main()

    elif selected == "Predict Defects":

        st.sidebar.subheader('Settings')

        options = st.sidebar.radio(
            'Options:', ('Image', 'Video'), index=1)

        st.sidebar.markdown("---")
        # Image
        if options == 'Image':
            upload_img_file = st.sidebar.file_uploader(
                'Upload Image', type=['jpg', 'jpeg', 'png'])
            if upload_img_file is not None:
                file_bytes = np.asarray(
                    bytearray(upload_img_file.read()), dtype=np.uint8)
                img = cv2.imdecode(file_bytes, 1)

                prediction = model.predict(img)
                res_plotted = prediction[0].plot()
                image_pil = Image.fromarray(res_plotted)
                image_bytes = io.BytesIO()
                image_pil.save(image_bytes, format='PNG')

                st.image(image_bytes, caption='Predicted Image',
                         use_column_width=True)

        if options == 'Video':
            upload_vid_file = st.sidebar.file_uploader(
                'Upload Video', type=['mp4', 'avi', 'mkv']
            )
            if upload_vid_file is not None:
                # Save the uploaded video file temporarily
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                temp_file.write(upload_vid_file.read())

                # Process the video frames and get the output video file path
                video_path_output = process_video(temp_file.name)

                # Display the processed video using the st.video function
                st.video(video_path_output)

                # Remove the temporary files
                temp_file.close()
                os.remove(video_path_output)

    elif selected == "Contributors":
        contributers.main()
    elif selected == "Model Information":
        model_information.main()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
