import face_recognition
import io
from PIL import Image
import numpy as np
def detect_face(img):
    try:
        img = Image.open(io.BytesIO(img.read())).convert('RGB')
        image_np = np.array(img)
        face_locations = face_recognition.face_locations(image_np)
        return len(face_locations) > 0
    except Exception as e:
        print(f"检测人脸时出错: {e}")
        return False
