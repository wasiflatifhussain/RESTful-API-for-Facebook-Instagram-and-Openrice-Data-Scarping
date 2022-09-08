
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
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import WebDriverException

# server imports
from server import app
from server.fb_routes import add_FBuser
from server.fb_queue import add_FBqueue, delete_FBqueue
from server.models.FB_Queue import FB_Queue
from server.models.FB_Adds import FB_Adds
from server.fb_add import delete_FBurl

import schedule
import time

from server import logmaker

def check_FBupdate():
    all_urls = FB_Adds.query.all()
    queue = FB_Queue.query.all()
    for link in all_urls:
        count = 0
        for element in queue:
            if (link.url == element.url):
                count += 1
        if (count == 0):
            add_FBqueue(link.url)
            delete_FBurl(link.url)
        if (count > 0):
            # print("Deleted unused URL.")
            logmaker.logger.info(f"Deleted unused URL.")
            delete_FBurl(link.url)
    pendings = 0
    for each in queue:
        if (each.status == "Pending"):
            pendings += 1
    if (pendings > 0):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options)

        # open the webpage
        driver.get("http://www.facebook.com")

        # target username
        username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

        # enter username and password
        username.clear()
        # username.send_keys("litroint@gmail.com")
        username.send_keys(app.config["FB_EMAIL"])
        password.clear()
        # password.send_keys("litroTEAM5435")
        password.send_keys(app.config["FB_PASS"])

        # target the login button and click it
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']"))).click()
        sleep(10)
    for each in queue:
                # calls add_to_db to add it to database
        if (each.status == "Pending"):
            add_to_db(driver, each.url)


def check_validity(driver, url):
    try:
        driver.get(f"{url}")

    except InvalidArgumentException:
        return False
    except WebDriverException:
        return False
    return True


def check_page_type(driver, url):
    try:
        driver.find_element(By.XPATH, "//div[@class='w0hvl6rk qjjbsfad']")
    except NoSuchElementException:
        return False
    return True


def add_to_db(driver, url):
    check = check_validity(driver, url)  # checks URL validity
    # driver.get(f"{url}")
    check_type = check_page_type(driver, url)

    if (check == True and check_type == True):
        check_err = driver.find_element(
            By.XPATH, "//div[@class='w0hvl6rk qjjbsfad']")
        if (check_err.text == "This page isn't available"):
            delete_FBqueue(url)
            logmaker.logger.info(f"The url: {url} is Invalid.")
            # print("Invalid URL")
            return

    # elif (check == False or check_type == False):
    #     delete_FBqueue(url)
    #     print("Invalid URL")
    #     return

    # gets profile name
    name = driver.find_element(
        By.XPATH, "//div[@class='mfn553m3 th51lws0']").text

# bi6gxh9e aov4n071
    def check_exists():  # checks if friendlist hidden or not and gets friends number
        try:
            driver.find_element(
                By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ll8tlv6m discj3wi']")
        except NoSuchElementException:
            return False
        return True

    check_friend = check_exists()
    if (check_friend == True):
        friends = driver.find_element(
            By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ll8tlv6m discj3wi']").text
    elif (check_friend == False):
        friends = "Friendlist Hidden."

    userid = url[25:]

    add_FBuser(userid, name, friends)

    # driver.quit()
    # sleep(50)
    sleep(app.config["INTERVAL"])  # 10
    delete_FBqueue(url)
    sleep(app.config["INTERVAL"])  # 10


# check every 20 minutes (1200 sec)
schedule.every(app.config["FB_TIME"]).seconds.do(check_FBupdate)
# app.config["FB_TIME"]

# time.sleep(10)

while True:
    schedule.run_pending()  # calls all scheduled tasks and makes them happen
    time.sleep(1)
    
    
    
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# from time import sleep
# from webbrowser import Chrome
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import InvalidArgumentException
# from selenium.common.exceptions import WebDriverException

# # server imports
# from server import app
# from server.fb_routes import add_FBuser
# from server.fb_queue import add_FBqueue, delete_FBqueue
# from server.models import FB_Queue, FB_Adds
# from server.fb_add import delete_FBurl

# import schedule
# import time


# def check_FBupdate():
#     all_urls = FB_Adds.query.all()
#     queue = FB_Queue.query.all()
#     for link in all_urls:
#         count = 0
#         for element in queue:
#             if (link.url == element.url):
#                 count += 1
#         if (count == 0):
#             add_FBqueue(link.url)
#             delete_FBurl(link.url)
#         if (count > 0):
#             print("Deleted unused URL.")
#             delete_FBurl(link.url)
#     pendings = 0
#     for each in queue:
#         if (each.status == "Pending"):
#             pendings += 1
    
#     if (pendings > 0):
#         chrome_options = webdriver.ChromeOptions()
#         prefs = {"profile.default_content_setting_values.notifications": 2}
#         chrome_options.add_experimental_option("prefs", prefs)

#         driver = webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()), options=chrome_options)

#         # open the webpage
#         driver.get("http://www.facebook.com")

#         # target username
#         username = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
#         password = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#         # enter username and password
#         username.clear()
#         # username.send_keys("litroint@gmail.com")
#         username.send_keys(app.config["FB_EMAIL"])
#         password.clear()
#         # password.send_keys("litroTEAM5435")
#         password.send_keys(app.config["FB_PASS"])

#         # target the login button and click it
#         button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
#             (By.CSS_SELECTOR, "button[type='submit']"))).click()
#         sleep(10)
#         for each in queue:
#                 # calls add_to_db to add it to database
#             if (each.status == "Pending"):    
#                 add_to_db(driver, each.url)


# def check_validity(driver, url):
#     try:
#         driver.get(f"{url}")

#     except InvalidArgumentException:
#         return False
#     except WebDriverException:
#         return False
#     return True


# def check_page_type(driver, url):
#     try:
#         driver.find_element(By.XPATH, "//div[@class='w0hvl6rk qjjbsfad']")
#     except NoSuchElementException:
#         return False
#     return True


# def add_to_db(driver, url):
#     check = check_validity(driver, url)  # checks URL validity
#     sleep(10)
#     # driver.get(f"{url}")
#     # check_type = check_page_type(driver, url)

#     # if (check == True and check_type == True):
#     #     check_err = driver.find_element(
#     #         By.XPATH, "//div[@class='w0hvl6rk qjjbsfad']")
#     #     if (check_err.text == "This page isn't available"):
#     #         delete_FBqueue(url)
#     #         print("Invalid URL")
#     #         return

#     if (check == False): #or check_type == False):
#         delete_FBqueue(url)
#         print("Invalid URL")
#         return
#     elif (check == True):
#         # gets profile name
#         name = driver.find_element(
#             By.XPATH, "//div[@class='bi6gxh9e aov4n071']").text

#         def check_exists():  # checks if friendlist hidden or not and gets friends number
#             try:
#                 driver.find_element(
#                     By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ll8tlv6m discj3wi']")
#             except NoSuchElementException:
#                 return False
#             return True

#         check_friend = check_exists()
#         if (check_friend == True):
#             friends = driver.find_element(
#                 By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ll8tlv6m discj3wi']").text
#         elif (check_friend == False):
#             friends = "Friendlist Hidden."

#         userid = url[25:]

#         add_FBuser(userid, name, friends)

#         # driver.quit()
#         # sleep(50)
#         sleep(app.config["INTERVAL"])  # 10
#         delete_FBqueue(url)
#         sleep(app.config["INTERVAL"])  # 10


# # check every 20 minutes (1200 sec)
# schedule.every(10).seconds.do(check_FBupdate)
# # app.config["FB_TIME"]

# # time.sleep(10)

# while True:
#     schedule.run_pending()  # calls all scheduled tasks and makes them happen
#     time.sleep(1)







