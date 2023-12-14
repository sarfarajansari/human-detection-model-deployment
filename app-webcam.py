from views import project_information, model_information
import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
from ultralytics import YOLO
import streamlit_option_menu as option_menu
from PIL import Image, ImageDraw
import io
import tempfile
import imageio.v2 as imageio
from moviepy.editor import ImageSequenceClip
import os
import av
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
model = YOLO('best.pt')


class web:
    def __init__(self):
        self.model = YOLO('best.pt')

    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")
        img = Image.fromarray(frm)
        results = self.model.predict(img)
        frame_bbx = results[0].plot()
        processed_frame = Image.fromarray(frame_bbx)
        return av.VideoFrame.from_ndarray(np.array(processed_frame), format="bgr24")


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

    st.title("AI Road Inspection System")
    Header = st.container()

    st.image("logo.png")
    # MainMenu

    with st.sidebar:
        selected = option_menu.option_menu(
            "Main Menu",
            options=[
                "Project Information",
                "Model Information",
                "Predict Defects",
                "Contributors"
            ],
        )

    st.sidebar.markdown('---')

    # HOME page

    if selected == "Project Information":
        project_information.main()

    elif selected == "Predict Defects":

        st.sidebar.subheader('Settings')

        options = st.sidebar.radio(
            'Options:', ('Image', 'Video', 'WebCam'), index=1)

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

                temp_file.close()
                os.remove(video_path_output)

        if options == 'WebCam':
            transformer = web()

            webrtc_ctx = webrtc_streamer(key="key", video_processor_factory=web, rtc_configuration=RTCConfiguration(
                {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}, async_processing=True,
            ))

            if webrtc_ctx:
                webrtc_ctx.recv = web().recv

                # Remove the temporary files

    elif selected == "Contributors":
        st.subheader("Contributors")
        st.markdown(
            "<b><u>Project Leads :</u></b> Eeman Majumder, Vaasu Bisht , Cesar Tinoco & Mario Rodriguez", unsafe_allow_html=True)
        st.markdown("<b><u>Management & HR:</u><b> Sakshi Sawarkar ",
                    unsafe_allow_html=True)
        st.markdown("<b><u>Project Contributors :</u></b> \n  ",
                    unsafe_allow_html=True)
        st.text(""" 1.  Adeeba Rashid \n 2.  Aditya Narayan Jha \n 3.  Akshit Srivastava \n 4.  Ameya Sharma \n 5.  Ananya Tiwari \n 6.  Annirudha Kumar \n 7.  Arjita Arora \n 8.  Ashwin J R \n 9.  Bhushan Kumar \n 10. Darshnik Rohal \n 11. Debadrita Dey \n 12. Devanshi Pathak \n 13. Enrique Unzueta \n 14. Jyotsna Bhatia \n 15. Mohit Kumar Saw \n 16. Mrunmayee Ketkar \n 17. Mudit Gaur \n 18. Navneet Lamba \n 19. Punit Kaushik \n 20. Pushpendra Kushwaha \n 21. Qurat ul aaein \n 22. Ram Vikram Singh \n 23. Sergio Reyes \n 24. Shreya Tripathi \n 25. Simone Reynoso \n 26. Soumyashis Sarkar \n 27. Sourav Dutta \n 28. Suhani Thakur \n 29. Swetha Thampi M \n 30. Tarandeep Singh Juneja \n 31. Yahya Ismaiel \n""")

    elif selected == "Model Information":
        model_information.main()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
