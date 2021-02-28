from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from function import say_stuff

driver = open("browser.txt", "r").read()
website = input(say_stuff("Which website would you like to go to?", False))
driver.get(website)
