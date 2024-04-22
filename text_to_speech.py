# Packages we need - pyttsx3

import pyttsx3

def text_to_speech(text):
    engin = pyttsx3.init()
    rate = engin.getProperty('rate')
    engin.setProperty('rate', rate-70)
    engin.say(text)
    engin.runAndWait()
