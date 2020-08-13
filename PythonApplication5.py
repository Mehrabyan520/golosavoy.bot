
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    #print(words)
    #os.system("say " + words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Привет, спроси у меня что-либо")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_theshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        harc = r.recognize_google(audio).lower() 
        print("Вы сказали: " + command)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        harc = command

    return harc


def makeSomthing(harc):
    if 'open website' in harc:
        talk("Ok")
        url = 'https://google.ru'
        webbrowser.open(url)
    elif 'stop' in harc:
        talk("Yes, ok")
        sys.exit()

while True:
    makeSomthing(command())