import csv
import time
from telnetlib import EC

import pandas as pd
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


def autoConnect(driver):
    csv_file_path = 'recourses/url_linkedin.csv'
    data = pd.read_csv('recourses/url_linkedin.csv')
    rows = []
    with open(csv_file_path, 'r', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        time.sleep(0.5)
        for value in range(len(rows) - 1):
            print("Value" + str(value))
            value1 = value
            link = data['LinkedIn_Link'][value1]
            driver.get(link)

            time.sleep(6)
            print('Try to click connect')
            try:
                followButon = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button")
                button_text1 = followButon.get_attribute("aria-label")
                if "Invite" in button_text1:
                    try:
                        followButon.click()
                        print("click connect!")
                        time.sleep(2)
                        connectButonNew = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
                        connectButonNew.click()
                        time.sleep(2)
                        checkStatus = followButon.get_attribute("aria-label")
                        if "Pending" in checkStatus:
                            print("Pending!" + data['LinkedIn_Link'][value])
                            writeCvs("Pending", value + 1)
                            print("write in csv!")
                        else:
                            print("Not connected one !" + data['LinkedIn_Link'][value])
                            writeCvs("Not Connected", value + 1)
                            print("write in csv!")
                    except NoSuchElementException:
                        print("Not connected one !" + data['LinkedIn_Link'][value])
                        writeCvs("Not Connected", value + 1)
                        print("write in csv!")
                elif "Follow" in button_text1:
                    try:
                        connectButonNew1 = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button")
                        connectButonNew1.click()
                        time.sleep(1)
                        connectButonNew2 = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div")
                        connectButonNew2.click()

                        connectButonNew3 = driver.find_element(By.XPATH,
                                                               "/html/body/div[3]/div/div/div[3]/button[2]")
                        connectButonNew3.click()
                        print('value: ' + str(value))
                        writeCvs("Pending", value + 1)
                        print("Connected!")
                    except NoSuchElementException:
                        print("Not connected one !" + data['LinkedIn_Link'][value])
                        writeCvs("Not Connected", value + 1)
                        print("write in csv!")
                elif "Pending" in button_text1:
                        print("Pending!" + data['LinkedIn_Link'][value])
                        writeCvs("Pending", value + 1)
                        print("write in csv!")
            except NoSuchElementException:
                try:
                    checkStatus = driver.find_element(By.XPATH,
                                                      "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button")
                    checkStatus.click()
                    time.sleep(1)
                    checkStatus = driver.find_element(By.XPATH,
                                                      "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[7]/div")
                    checkStatus2 = checkStatus.get_attribute("aria-label")
                    if "Remove" in checkStatus2:
                        print("Connected!" + data['LinkedIn_Link'][value])
                        writeCvs("Pending", value + 1)
                        print("write in csv!")
                except NoSuchElementException:
                    print("Not Connected" + data['LinkedIn_Link'][value])
                    writeCvs("Not Connected", value + 1)
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
