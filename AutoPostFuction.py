from datetime import datetime, time
from PostFuction import postOnLinkedIn
from selenium.webdriver.common.by import By
from datetime import time, datetime
import time as time

def autoPostFuction(driver,alarmUi):
    alarm = alarmUi #recive from Gui
    current_time = "Son tung mtp"
    while(alarm!=current_time):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time)
    postOnLinkedIn(driver)
