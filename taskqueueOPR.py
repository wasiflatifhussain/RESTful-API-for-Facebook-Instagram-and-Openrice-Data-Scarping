from webbrowser import Chrome
import pandas as pd
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import schedule
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import WebDriverException


from server.opr_routes import add_OPRuser
from server.opr_queue import add_OPRqueue, delete_OPRqueue
from server .models import OPR_Queue, OPR_Adds
from server.models.OPR_Queue import OPR_Queue
from server.models.OPR_Adds import OPR_Adds
from server.opr_add import delete_OPRurl
from server import app


def check_OPR_update():  # checks if there are new tasks in the queue present 
    all_urls = OPR_Adds.query.all()
    queue = OPR_Queue.query.all()
    for link in all_urls:
        count = 0
        for element in queue:
            if (link.url == element.url):
                count += 1
        if (count == 0):
            add_OPRqueue(link.url)
            delete_OPRurl(link.url)       
    
    # total = 0
    pendings = 0
    for each in queue:
        if (each.status == "Pending"):
            pendings += 1
            
    if (pendings > 0):
        driver = webdriver.Chrome(service=Service(  # opens the driver once and can be used for multiple
            ChromeDriverManager().install()))
            # for each in queue:
                # calls add_to_db to add it to database
    for each in queue:
        if (each.status == "Pending"):
            add_to_db_OPR(driver, each.url)


# checks the validity of the urls sent to first check if they are valid openrice urls
def check_OPR_validity(driver, url):
    try:
        driver.get(f'{url}')
    except InvalidArgumentException:
        return False
    except WebDriverException:
        return False
    return True


# checks to see if the urls actually open into an openrice user profile or not
def check_OPR_tag(driver):
    try:
        driver.find_element(By.ID, 'user_username')
    except NoSuchElementException:
        return False
    return True


# if all criteria are met and the url is valid, it visits the url and adds data to main database
def add_to_db_OPR(driver, url):
    # driver.get(f'{url}')
    check = check_OPR_validity(driver, url)
    if (check == False):
        delete_OPRqueue(url)
        sleep(10)
        return

    elif (check == True):
        check2 = check_OPR_tag(driver)
        if (check2 == False):
            delete_OPRqueue(url)
            sleep(10)
            return
    username = driver.find_element(By.ID, 'user_username').text
    level = driver.find_element(By.XPATH, "//div[@class='txt_13 MT5']").text
    followInfo = driver.find_elements(By.XPATH, "//div[@class='count']")
    followings = followInfo[0].text
    followers = followInfo[1].text
    add_OPRuser(username, level, followings, followers)
    sleep(app.config["INTERVAL"])  # 10
    delete_OPRqueue(url)  # deletes the added user link from the queues
    sleep(app.config["INTERVAL"])  # 10


# check every 5 minutes(900)
schedule.every(app.config["OPR_TIME"]).seconds.do(check_OPR_update)

while True:
    schedule.run_pending()  # calls all scheduled tasks and makes them happen
    time.sleep(1)

