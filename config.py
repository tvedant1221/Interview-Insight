# config.py

# Configuration for language tool settings
LANGUAGE_TOOL_LANGUAGE = 'en-US'  # English (US)
GRAMMAR_CHECK_THRESHOLD = 75.0    # Minimum grammar accuracy for a positive evaluation

# Camera settings
VIDEO_CAPTURE_INDEX = 0           # Default camera index (0 for built-in webcam)
CAMERA_FRAME_WIDTH = 640          # Width of the video frame for facial recognition
CAMERA_FRAME_HEIGHT = 480         # Height of the video frame for facial recognition

# Keyword evaluation
KEYWORD_MATCH_THRESHOLD = 50.0    # Minimum keyword match percentage for a good score

# Text-to-speech settings
TTS_ENGINE_RATE = 150             # Speed of speech (adjust for faster/slower speech)
TTS_ENGINE_VOLUME = 0.9           # Volume level (0.0 to 1.0)

# Flask app settings
DEBUG_MODE = True                 # Enable/disable debug mode for Flask app
PORT = 5000                       # Port on which Flask app runs
HOST = "0.0.0.0"                  # Host address for running the app

# Facial expression detection settings
EMOTION_ANALYSIS_INTERVAL = 1.0   # Interval in seconds between emotion analysis frames
