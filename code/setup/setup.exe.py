import os
import wget
import shutil
working_dir = os.getcwd()
os.makedirs("python")
wget.download("https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/setup/python-3.9.0-embed-win32.zip", "python/")
shutil.unpack_archive("python/python-3.9.0-embed-win32.zip", "python/", "zip")
os.remove("python/python-3.9.0-embed-win32.zip")
os.system(working_dir + "\\python\\python.exe get-pip.py")
os.system(working_dir + "\\python\\python.exe -m pip --upgrade pip")
os.system(working_dir + "\\python\\python.exe setup.py")
