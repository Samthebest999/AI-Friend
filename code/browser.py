import pyautogui

from functions import say_stuff
from imports import sr
from imports import time
browser = str(open("browser.txt", "rt").read())


def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        global users_text
        users_text = r.recognize_google(audio)


say_stuff("Hi, Which website would you like to go to?", False)
users_text = input("Which website would you like to go to?")
website = " https://" + users_text
pyautogui.hotkey("winleft", "r")
time.sleep(.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(.5)
pyautogui.press("backspace")
time.sleep(.5)
pyautogui.write(browser + website)
time.sleep(.5)
pyautogui.press("enter")
