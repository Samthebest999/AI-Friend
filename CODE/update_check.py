from imports import wget, os

open_toml = open("version.toml", "r").read()
vtu = "https://raw.githubusercontent.com/Samthebest999/AI-Friend/main/CODE/version.toml"
wget.download(vtu)
new_open_toml = open("version.toml", "r").read()
if open_toml == new_open_toml:
    quit()
if open_toml != new_open_toml:
    os.system("updater.py")
