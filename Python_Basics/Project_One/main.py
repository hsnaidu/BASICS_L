# Project Install : pyaudio, speechrecognition, setuptools, webbrowser (Builtin-module), pyttsx3 (text to speech reco)

import speech_recognition as sr
import webbrowser as wb
import pyttsx3

# Init Sr. Recoginizer
reco = sr.Recognizer()
# Init Enging-Parameter
engine = pyttsx3.init()

def speak(txt):
    engine.say(txt)
    engine.runAndWait()
        

def observe():
    with sr.Microphone() as source:
        print('Say something')
        audio = reco.listen(source)
        return audio
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

if __name__ == "__main__":  # This will help in runnig the script directly , If i import script into another file 
    
    observe()