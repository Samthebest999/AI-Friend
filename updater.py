import os
import wget

os.remove("browser.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/browser.py")
os.remove("functions.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/functions.py")
os.remove("imports.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/imports.py")
os.remove("main.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/main.py")
os.system("python main.py")
