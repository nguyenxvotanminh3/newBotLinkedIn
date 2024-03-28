import csv
import time
from telnetlib import EC

import pandas as pd
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


def autoConnect(driver):

    keyboard = Controller()
    csv_file_path = 'recourses/url_linkedin.csv'
    data = pd.read_csv('recourses/url_linkedin.csv')
    rows = []
    with open(csv_file_path, 'r', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Enter the URL for 2nd Connections
    # value 0, 1, 2, 3, 4
    for value in range(len(rows) - 1):
        print("Value" + str(value))
        value1 = value
        try:
            link = data['LinkedIn_Link'][value1]
            # Thay 'LinkedIn_Link' bằng tên cột chứa URL LinkedIn
            # Kiểm tra URL của người dùng trên LinkedIn
            # Mở URL trên trình duyệt
            driver.get(link)
            time.sleep(2)
            print('Try to click connect')
            followButon = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button")
            followButon.click()
            time.sleep(2)
            print("click connect!")
            time.sleep(2)
            connectButonNew = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
            connectButonNew.click()
            time.sleep(1)
            print("click Send without comment!")
            #first input
            #last input
            # if(value == len(rows) - 1):
            #     value = value + 1
            print('value: ' + str(value))
            writeCvs("Done",value + 1)
            print("write in csv: connected one!")
        except NoSuchElementException:
            # if (value == len(rows) - 1):
            #     value = value + 1
            print('value: ' + str(value))
            print("Not connected one !" + data['LinkedIn_Link'][value])
            writeCvs("Not Connected",value + 1)
            print("write in csv!")


def writeCvs(text,rowInLoop):
    csv_file_path = 'recourses/url_linkedin.csv'
    # Read existing data
    rows = []
    with open(csv_file_path, 'r', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        rows[rowInLoop][1] = text
    # Modify data for the first row
    with open(csv_file_path, 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
