import configparser
import os
import sys
from telnetlib import EC
from datetime import datetime

import pyautogui
import selenium
from msedge.selenium_tools import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def Login_Linkedin(driver):
    baseDir = os.path.dirname(os.path.realpath(sys.argv[0])) + os.path.sep
    """ Setup Argument Parameters """
    config = configparser.RawConfigParser()
    config.read(baseDir + 'recourses/Account.cfg')
    username = config.get('CREDS', 'linkedin_username')
    password = config.get('CREDS', 'linkedin_password')
    print(username, password)
    # head to  login page
    driver.get("https://www.linkedin.com/home")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input").send_keys(password)
    time.sleep(0.5)
    # click login button
    text_button = driver.find_element(By.XPATH,
                                      "/html/body/main/section[1]/div/div/form/div[2]/button")
    # wait for check robot
    text_button.click()
