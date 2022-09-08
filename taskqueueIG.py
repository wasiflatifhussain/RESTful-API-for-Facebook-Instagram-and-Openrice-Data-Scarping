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


from server.ig_routes import add_IGuser
from server.ig_queue import add_IGqueue, delete_IGqueue
from server .models import IG_Queue, IG_Adds
from server.models.IG_Queue import IG_Queue
from server.models.IG_Adds import IG_Adds
from server.ig_add import delete_IGurl
from server import app


from http.client import UNSUPPORTED_MEDIA_TYPE
from itertools import count
from instagram_scraper.constants import STORIES_UA
from instagram_scraper import InstagramScraper
scraper = InstagramScraper()
scraper.authenticate_as_guest()



def check_IG_update():  # checks if there are new tasks in the queue present 
    all_urls = IG_Adds.query.all()
    queue = IG_Queue.query.all()
    for link in all_urls:
        count = 0
        for element in queue:
            if (link.url == element.url):
                count += 1
        if (count == 0):
            add_IGqueue(link.url)
            delete_IGurl(link.url)       
    
    # total = 0
    pendings = 0
    for each in queue:
        if (each.status == "Pending"):
            pendings += 1
            
    # if (pendings > 0):
    #     driver = webdriver.Chrome(service=Service(  # opens the driver once and can be used for multiple
    #         ChromeDriverManager().install()))
            # for each in queue:
                # calls add_to_db to add it to database
    for each in queue:
        if (each.status == "Pending"):
            add_to_db_IG(each.url)


# checks the validity of the urls sent to first check if they are valid openrice urls
def check_IG_validity(person):
    try:
        person["edge_followed_by"]["count"]
    except TypeError:
        return False
    return True


# checks to see if the urls actually open into an openrice user profile or not
# def check_IG_tag(driver):
#     try:
#         driver.find_element(By.ID, 'user_username')
#     except NoSuchElementException:
#         return False
#     return True


# if all criteria are met and the url is valid, it visits the url and adds data to main database
def add_to_db_IG(url):
    link = url
    username = link[26:-1:]
    scraper.session.headers.update({'user-agent': STORIES_UA})
    user = scraper.get_shared_data_userinfo(username)
    # user = scraper.session.get('_safwan.ahmed_')
    check = check_IG_validity(user)
    if (check == False):
      delete_IGqueue(url)
      return
    elif (check == True):
      followers = user["edge_followed_by"]["count"]
      followings = user["edge_follow"]["count"]
      # userID = user["id"]
      add_IGuser(username, followers, followings)
      sleep(app.config["INTERVAL"])  # 10
      delete_IGqueue(url)  # deletes the added user link from the queues
      sleep(app.config["INTERVAL"])  # 10


# check every 5 minutes(900)
schedule.every(app.config["IG_TIME"]).seconds.do(check_IG_update)

while True:
    schedule.run_pending()  # calls all scheduled tasks and makes them happen
    time.sleep(1)

