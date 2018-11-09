import time
from datetime import datetime, timedelta
import math

now = datetime.now()

# start the script at 4 am
year = now.year
month = now.month
day = now.day  # next day
hour = now.hour  # 4 am
minute = now.minute
second = now.second + 10
later = datetime(year, month, day, hour, minute, second)
seconds = (later - now).total_seconds()
print("Starting the script at " + str(later) + "...")

d = datetime(1, 1, 1) + timedelta(seconds=seconds)

print("Starting in: %d days %d hours %d minutes %d seconds" % (d.day - 1, d.hour, d.minute, d.second))
# print("Waiting " + str(math.floor(seconds / 60 / 60)) + " hours " + str(math.floor(seconds / 60)) + " minutes " + str(seconds) + " seconds.")

time.sleep(seconds)
print(str(seconds) + " seconds have passed...")
