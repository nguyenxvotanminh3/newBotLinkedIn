import time
from datetime import datetime


alarm = "22:18:00"
current_time = "Ngon"
while(alarm!=current_time):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time.sleep(1)
    print(current_time)

print("alarm")