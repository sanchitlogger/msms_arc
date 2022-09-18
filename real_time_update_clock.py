
import time
import sys
import datetime

while True:
    now = datetime.datetime.now()
    print(now.strftime("%HH:%MM:%SS"), end="\r")
    sys.stdout.flush()