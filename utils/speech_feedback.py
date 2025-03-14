import pyttsx3
from config import TTS_ENGINE_RATE, TTS_ENGINE_VOLUME

def provide_feedback(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', TTS_ENGINE_RATE)  # Speed of speech
    engine.setProperty('volume', TTS_ENGINE_VOLUME)  # Volume level
    engine.say(text)
    engine.runAndWait()
