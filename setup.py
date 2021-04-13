import os
os.system("pip3 install wget")
import wget


class DownloadRequiredFiles:
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/browser.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/functions.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/imports.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/main.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/requirements.txt")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/version.toml")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/updater.py")
    print("Please Wait as I install the important packages needed...")
    os.system("pip install -r requirements.txt && pipwin refresh && pipwin install pyaudio ")


from functions import say_stuff


class NameStuff:
    print("Welcome to the AI Friend!")
    global name
    name = input("Hi, What is your **FIRST** name?")
    if name == "":
        print("Oops. Your name is empty")
        name = input("Hi, What is your **FIRST** name?")
    else:
        print("Ok, Hi " + name + "!")
    UserNameWrite = open("UserNameStuff.txt", "w")
    UserNameWrite.write(name)
    UserNameWrite.close()


class BirthDay:
    print("Ok " + name + ", After learning your name I feel a lot better!")
    BirthDate = input("When is your birthday? (Please enter it in the format MM/DD/YYYY)")
    if BirthDate == "":
        print("Oops Your Birthdate is empty!")
        BirthDate = input("When is your birthday? (Please enter it in the format MM/DD/YYYY)")
    else:
        UserBirthDateStuffWrite = open("UserBirthDateStuff.txt", "w")
        UserBirthDateStuffWrite.write(BirthDate)
        UserBirthDateStuffWrite.close()


class Browser:
    ub = input("Ok, ""Which browser do you use? Firefox, Chrome, or Microsoft Edge? ")
    ub = ub.lower()
    if ub == "microsoft edge":
        obdtc = open("browser.txt", "w+").write("msedge")
        quit(say_stuff("Done With The Setup", False))
    obdtc = open("browser.txt", "w+").write(ub.lower())
    obdtc.close()
