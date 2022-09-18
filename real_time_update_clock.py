import time
import sys
import datetime

while True:
    now = datetime.datetime.now()
    print(now.strftime("%HH:%MM:%SS"), end="\r")
    sys.stdout.flush()
    sys.stdout.flush() # everyting is fuffers to terminal
    time.sleep(0.1) # prints after every 0.1 seconds