import pyautogui

from functions import say_stuff
from imports import sr, time

browser = str(open("browser.txt", "rt").read())


users_text = input(say_stuff("Hi, Which website would you like to go to?", False))
website = " https://" + users_text
pyautogui.hotkey("winleft", "r")
time.sleep(0.50)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
pyautogui.write(browser + website)
time.sleep(0.50)
pyautogui.press("enter")