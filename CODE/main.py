from function import *
from imports import *


# TODO GET A BETTER NAME FOR THE PROGRAM!

class VoiceRecogError(Exception):
    pass


def recog_stuff():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        global what_user_said
        what_user_said = r.recognize_google(audio)


class CheckForUpdates:
    os.system("update_check.py")


class SetupStuff:
    lang = 'en'
    wc = "Hi! Welcome to your AI Friend!"
    print(wc)
    say_stuff(wc, False)
    say_stuff("Would you like to go through the setup process?", False)
    setup = input("Would you like to go through the setup process??")
    if setup == "Yes":
        url = "https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/OTHER%20STUFF/setup.exe"
        wget.download(url)
        os.system("setup.exe")
    elif setup == "yes":
        url = "url"
        wget.download(url, "/")
        os.system("setup.exe")
    else:
        say_stuff("Ok", False)


class AI:
    stuff = 0
    ouns = open("UserNameStuff.txt", "r")
    rouns = ouns.read()
    ouns.close()
    while stuff == 0:
        say_stuff("Hi, " + rouns, False)
        try:
            recog_stuff()
        except:
            raise VoiceRecogError(say_stuff(
                "Microphone error, Possible reasons: Too much background noise, microphone off, couldn't hear you, "
                "your accent, or just program couldn't recognize your voice",
                False), "Microphone error, Possible reasons: Too much background noise, microphone off, couldn't hear "
                        "you, "
                        "your accent, or just program couldn't recognize your voice")
        User_Input = what_user_said
        if User_Input == "help":
            help_menu = """Hi Welcome To The Help Menu!
            So far you can say "Hi"
            or "help"            
            
            """
            print(help_menu)
            say_stuff(help_menu, False)
        if User_Input == "hi":
            say_stuff("Hello, " + rouns, False)
