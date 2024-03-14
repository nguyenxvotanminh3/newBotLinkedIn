from random import random

import pandas as pd
import datetime
from datetime import time
import time as time
import pyautogui
from pynput import keyboard
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


def postOnLinkedIn(driver):
    keyboard = Controller()
    df = pd.read_csv('recourses/Content.csv')
    time.sleep(5)
    # text_button = driver.find_element(By.XPATH,
    #                                   "//button[contains(@class, 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger')]")
    # text_button.click()


    #click in media button
    text_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary share-box-feed-entry-toolbar__item')]")
    text_button.click()
    time.sleep(5)
    keyboard.type('D:\Test\est1.jpg')
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    next = driver.find_element(By.ID, "ember196")
    next.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys(df['Content'][0])
    time.sleep(random.randint(3, 9))
    post_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]")
    post_button.click()