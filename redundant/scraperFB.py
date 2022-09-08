from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from time import sleep
from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# imports from server
from server.fb_routes import delete_FBuser
from server.fb_queue import add_FBqueue

do = input("POST or DELETE or END?: ")  # take the user request

while (do != "END"):
    if (do == "POST"):
        user = input("Please enter the user profile URL:- ")
        # adds new entries to the queue to be processed and added to main db
        add_FBqueue(user)
        do = input("POST or DELETE or END?: ")

    elif (do == "DELETE"):
        username = input("Enter the user's User ID: ")
        delete_FBuser(username)  # deletes the fb user by username(for dev use)
        do = input("POST or DELETE or END?: ")
