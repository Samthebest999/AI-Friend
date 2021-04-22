import os
import wget
import shutil

open("pythoninstalled.txt", "x")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/tests/pythoncheck.py")
os.system("python pythoncheck.py")
pythoninstalled = open("pythoninstalled.txt", "r").read()
if pythoninstalled == "True":
    wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/setup.py")
    os.system("python setup.py")
else:
    os.makedirs("python")
    wget.download("https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-win32.zip", "python/")
    shutil.unpack_archive("python/python-3.9.0-embed-win32.zip", "python/", "zip")
    os.remove("python/python-3.9.0-embed-win32.zip")
    os.system("setx path \"%path%;python/\"")
