from webbrowser import Chrome
import pandas as pd
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#imports from server.py
from server.opr_routes import delete_OPRuser
from server.opr_queue import add_OPRqueue


do = input("POST or DELETE or END?: ")
while (do != "END"):
    if (do == "POST"):
        user = input("Please enter the user profile URL:- ")
        # adds new entries to the queue to be processed and added to main db
        add_OPRqueue(user)
        do = input("POST or DELETE or END?: ")

    elif (do == "DELETE"):  # delete directly from the main users tables
        username = input("Enter the username: ")
        # implement a delete method using username instead of user id
        delete_OPRuser(username)
        do = input("POST or DELETE or END?: ")
        # loop through the user query all and find the name and delete that object element
