# Packages we need - PyAudio and SpeechRecognition==3.8.1

import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    # Handle the exceptional case...
    try:
        voice_data = ""
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError as e:
        print("Request error")





