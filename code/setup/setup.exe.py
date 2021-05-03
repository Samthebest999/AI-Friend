import os
import wget
import shutil
working_dir = os.getcwd()
os.makedirs("python")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/setup/python.zip", "python/")
shutil.unpack_archive("python/python.zip", "python/", "zip")
os.remove("python/python.zip")
os.system(working_dir + "\\python\\python.exe python\\get-pip.py")
os.system(working_dir + "\\python\\python.exe -m pip install pip wheel setuptools wget")
os.system(working_dir + "\\python\\python.exe -m pip install --upgrade pip wheel setuptools")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/code/setup.py")
os.system(working_dir + "\\python\\python.exe setup.py")
