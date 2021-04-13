import os
import wget
os.remove("browser.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/browser.py")
os.remove("functions.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/functions.py")
os.remove("imports.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/imports.py")
os.remove("main.py")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/main.py")
os.system("python main.py")
