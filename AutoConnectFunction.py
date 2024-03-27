import time
from telnetlib import EC

import pandas as pd
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


def autoConnect(driver):
    keyboard = Controller()
    data = pd.read_csv('recourses/url_linkedin.csv')
    print(data['LinkedIn_Link'])
    # Enter the URL for 2nd Connections
    for value in range(len('Index')+1):
            link = data['LinkedIn_Link'][value]  # Thay 'LinkedIn_Link' bằng tên cột chứa URL LinkedIn
            # Kiểm tra URL của người dùng trên LinkedIn

            # Mở URL trên trình duyệt
            driver.get(link)
            time.sleep(2)
            print('Try to click follow or connect')
            followButon = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button")
            followButon.click()


            time.sleep(3)
            print("click follow or connect!")
            print("find send without note if it's connect")
            time.sleep(3)
            connectButonNew = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
            connectButonNew.click()
            print("Click send without note!")




