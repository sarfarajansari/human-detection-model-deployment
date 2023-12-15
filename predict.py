import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io


model = YOLO('best.pt')


def predict(upload_img_file):
    file_bytes = np.asarray(
        bytearray(upload_img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    prediction = model.predict(img)
    res_plotted = prediction[0].plot()
    image_pil = Image.fromarray(res_plotted)
    image_bytes = io.BytesIO()
    image_pil.save(image_bytes, format='PNG')

    return image_bytes
