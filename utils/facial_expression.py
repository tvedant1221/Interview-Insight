import cv2
from deepface import DeepFace
import threading
from config import VIDEO_CAPTURE_INDEX, CAMERA_FRAME_WIDTH, CAMERA_FRAME_HEIGHT, EMOTION_ANALYSIS_INTERVAL

# Global variables
emotion_count = {
    'happy': 0,
    'sad': 0,
    'neutral': 0,
    'angry': 0,
    'surprise': 0,
    'fear': 0,
    'disgust': 0
}
camera_active = True

def capture_facial_expressions():
    global camera_active
    cap = cv2.VideoCapture(VIDEO_CAPTURE_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_FRAME_HEIGHT)
    while cap.isOpened() and camera_active:
        ret, frame = cap.read()
        if not ret:
            break
        
        try:
            analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = analysis[0]['dominant_emotion']
            emotion_count[dominant_emotion] += 1
        except Exception as e:
            print(f"Error in detecting expression: {str(e)}")

    cap.release()
    cv2.destroyAllWindows()

def start_facial_expression_thread():
    global camera_active
    camera_active = True
    facial_thread = threading.Thread(target=capture_facial_expressions)
    facial_thread.start()

def stop_camera():
    global camera_active
    camera_active = False
