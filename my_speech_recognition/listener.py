import sounddevice as sd
import numpy as np
import speech_recognition as sr

def listen(duration=5, samplerate=44100):
    # Capture audio
    print("Listening...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait for the recording to finish

    # Convert the NumPy array to audio data
    audio_data = np.frombuffer(recording, dtype=np.int16)

    # Initialize speech recognition
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)

    # Recognize speech using Google's speech recognition
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
