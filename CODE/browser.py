from functions import say_stuff
from imports import os, sr

browser = str(open("browser.txt", "rt"))


def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        global users_text
        users_text = r.recognize_google(audio)


say_stuff("Hi, Which website would you like to go to?", False)
recognize_speech()
website = " https://" + users_text
os.system(browser + website)
