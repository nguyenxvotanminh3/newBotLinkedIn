import pandas as pd
from datetime import time
import time as time
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller



def postOnLinkedIn(driver):

    keyboard = Controller()
    #take all the Content avaiable from resources
    df = pd.read_csv('recourses/Content.csv')
    time.sleep(5)
    # the ui will chose which content row
    i = 0
    choose = df['Image'][rowGet]
    #click in media button
    text_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary share-box-feed-entry-toolbar__item')]")
    text_button.click()
    time.sleep(5)
    #chose pic
    keyboard.type(choose)
    time.sleep(2)
    # hit enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    #click to next to paste content
    next = driver.find_element(By.XPATH, "//button[contains(@class, 'share-box-footer__primary-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]")
    next.click()
    time.sleep(2)

    #converte object of tag to string
    stringTag = str(df['Tag'][rowGet])

    #convert those into separeted string without comma
    converted = stringTag.split(",")



    #loop through name and put before name the '@' in oder to tag may be ???
    #this will loop through all the tag

    # -----Post with tag--------------------------------------------------------------------------------------------

    for value in range(len(converted)):
        driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys('@' + converted[value])
        time.sleep(5)
        keyboard.press(Key.down)
        time.sleep(2)
        keyboard.press(Key.enter)
        time.sleep(2)
        keyboard.press(Key.space)
    #--------------------------------------------------------------------------------------------------------------



    # --------------------------------------------------------------------------------------------------------------
    keyboard.press(Key.enter)
    driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys(df['Content'][rowGet])
    time.sleep(9)

    post_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]")
    post_button.click()


def reciveFromUi(row):
    global rowGet
    rowGet = row
    return rowGet
    time.sleep(1)