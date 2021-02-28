from imports import pyderman as driver
from imports import wget


class DownloadOtherStuff:
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/browser.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/function.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/imports.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/update_check.py")
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/updater.py")


class NameStuff:
    print("Welcome to the AI Friend!")
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
    print("Ok, After learning your name I feel a lot better!")
    print("I'm Pretty sure that you want to answer the next thing for sure and correctly because there is a small "
          "easter egg included! (Hint it is on your next birthday)")
    BirthDate = input("When is your birthday? (Please enter it in the format MM/DD/YYYY)")
    if BirthDate == "":
        print("Oops Your Birthdate is empty!")
        BirthDate = input("When is your birthday? (Please enter it in the format MM/DD/YYYY)")
    else:
        UserBirthDateStuffWrite = open("UserBirthDateStuff.txt", "w")
        UserBirthDateStuffWrite.write(BirthDate)
        UserBirthDateStuffWrite.close()


class Browser:
    ub = input("Which browser do you use? Firefox or Chrome")
    if ub == "Firefox":
        path = driver.install(browser=driver.firefox)
    elif ub == "firefox":
        path = driver.install(browser=driver.firefox)
    if ub == "Chrome":
        path = driver.install(browser=driver.chrome)
    elif ub == "chrome":
        path = driver.install(browser=driver.chrome)
    obdtc = open("browser.txt", "w+").write(ub.lower())
    obdtc.close()
