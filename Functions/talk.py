import pyttsx3
import speech_recognition as sr

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_running = False  # Flag to check if the engine is already running

# Function to convert text to speech
def talk(text):
    global engine_running
    engine.say(text)
    
    # Run the engine only if it's not already running
    if not engine_running:
        engine_running = True
        engine.runAndWait()
        engine_running = False
