import array

import pandas as pd
from datetime import time, datetime
import time as time
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller



def postOnLinkedIn(driver):
    keyboard = Controller()
    #loop from start to end
    for value1 in range(rowGetStart, rowGetEnd+1):
        driver.get("https://www.linkedin.com/home")
    #take all the Content avaiable from resources
        df = pd.read_csv('recourses/Content.csv')
        time.sleep(3)
    # the ui will chose which content row
        choose = df['Image'][value1]
        rawString=r"{}".format(choose)
        #click in media button
        text_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary share-box-feed-entry-toolbar__item')]")
        text_button.click()
        time.sleep(3)
        #chose pic
        keyboard.type(rawString)
        # hit enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        #click to next to paste content
        next = driver.find_element(By.XPATH, "//button[contains(@class, 'share-box-footer__primary-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]")
        next.click()


        # -TopHastag---------------------------------------------------------------------------------------
        # converte object of Hastag to string
        stringHastag = str(df['TopHastag'][value1])

        # convert those into separeted string without comma
        convertedTopHasTag = stringHastag.split(",")

        for value in range(len(convertedTopHasTag)):
            driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys('#' + convertedTopHasTag[value])
            keyboard.press(Key.space)
                       # --------------------------------------------------------------------------

        # --Content-------------------------------------------------------------------------------------------------

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys(df['Content'][value1])
        time.sleep(1)

        # ---Tag------------------------------------------------------------------------------------------

        keyboard.press(Key.enter)
        # converte object of tag to string
        stringTag = str(df['Tag'][value1])
        # convert those into separeted string without comma
        convertedTag = stringTag.split(",")

        # -----Post with tag--------------------------------------------------------------------------------------------
        count = 0
        for value in range(len(convertedTag)):
            count = count+1
            if (count == 4):
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(0.5)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                count = 0

            driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys('@'+convertedTag[value])
            time.sleep(3)
            keyboard.press(Key.down)
            time.sleep(0.5)
            keyboard.press(Key.enter)
            time.sleep(0.5)
            keyboard.press(Key.space)
            time.sleep(0.5)


        # --BotHastag-------------------------------------------------------------------------------------------------
        keyboard.press(Key.enter)
        # converte object of Hastag to string
        stringBotHastag = str(df['BotHastag'][value1])

        # convert those into separeted string without comma
        convertedBotHasTag = stringBotHastag.split(",")

        for value in range(len(convertedBotHasTag)):
            driver.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys('#' + convertedBotHasTag[value])

            keyboard.press(Key.space)

        # --------------------------------------------------------------------------------------------------------------

        post_button = driver.find_element(By.XPATH,
                                          "//button[contains(@class, 'share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]")
        post_button.click()
        time.sleep(15)


def reciveFromUi(rowStart, rowEnd):
    global rowGetStart
    global rowGetEnd
    rowGetStart = rowStart
    rowGetEnd = rowEnd
    return rowGetStart,rowGetEnd
    time.sleep(1)

