import os

from functions import *
from imports import *

if os.path.exists("setup.py"):
    os.remove("setup.py")
if os.path.exists("updater.py"):
    os.remove("updater.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/updater.py")


def update():
    open_toml = open("version.toml", "r").read()
    if os.path.exists("version.toml"):
        os.remove("version.toml")
    vtu = "https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/version.toml"
    wget.download(vtu)
    new_open_toml = open("version.toml", "r").read()
    if open_toml == new_open_toml:
        pass
    if open_toml != new_open_toml:
        working_dir = os.getcwd()
        os.system(working_dir + "\\python\\python.exe updater.py")
        quit(say_stuff("Updating...", False))


def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        global users_text
        users_text = r.recognize_google(audio)

update()
# TODO GET A BETTER NAME FOR THE PROGRAM!

class VoiceRecogError(Exception):
    pass


class AI:
    stuff = 0
    ouns = open("UserNameStuff.txt", "r")
    rouns = ouns.read()
    ouns.close()
    while stuff == 0:
        say_stuff("Hi, " + rouns, False)
        try:
            recognize_speech()
        except:
            raise VoiceRecogError(say_stuff(
                "Microphone error, Possible reasons: Too much background noise, microphone off, couldn't hear you, "
                "your accent, or just program couldn't recognize your voice",
                False), "Microphone error, Possible reasons: Too much background noise, microphone off, couldn't hear "
                        "you, "
                        "your accent, or just program couldn't recognize your voice")
        user_input = users_text
        if user_input == "help":
            helpdict = {"Hi": "Says Hello back to you", "browser": "go to the website of your choice"}
            help_menu = """Hi Welcome To The Help Menu!\n""" + helpdict
            print(help_menu)
            say_stuff(help_menu, False)
        if user_input == "hi":
            say_stuff("Hello, " + rouns, False)
        if user_input == "browser":
            working_dir = os.getcwd()
            os.system(working_dir + "\\python\\python.exe browser.py")
        if user_input == "update":
            update()
