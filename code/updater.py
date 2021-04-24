import os
import wget

os.remove("browser.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/browser.py")
os.remove("functions.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/functions.py")
os.remove("imports.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/imports.py")
os.remove("main.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/main.py")
working_dir = os.getcwd()
os.system(working_dir + "\\python\\python.exe main.py")