import os
import wget

#TODO GET A BETTER NAME FOR THE PROGRAM!


class SetupStuff:
    print("Hi! Welcome to the AI Friend!")
    setup = input("Would you like to go through the setup process??")
    if setup == "Yes":
        url = "url"
        wget.download(url, "/")
        os.system("setup.exe")
    elif setup == "yes":
        url = "url"
        wget.download(url, "/")
        os.system("setup.exe")
