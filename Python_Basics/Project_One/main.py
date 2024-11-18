# Project Install : pyaudio, speechrecognition, setuptools, webbrowser (Builtin-module), pyttsx3 (text to speech reco)

import speech_recognition as sr
import webbrowser as wb
import pyttsx3

# Init Sr. Recoginizer
reco = sr.Recognizer()
# Init Enging-Parameter
engine = pyttsx3.init()

class robot:
    
    @staticmethod
    def speak(txt):
        engine.say(txt)
        engine.runAndWait()

if __name__ == "__main__":  # This will help in runnig the script directly , If i import script into another file 
    
    me = robot()
    me.speak(input('enter your name : '))