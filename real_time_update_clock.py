import time
import sys
import datetime


while True:
    now = datetime.datetime.now()
    print(now,end="\r" )
    sys.stdout.flush()  # everyting is buffers to terminal
    time.sleep(0.1)  # prints after every 0.1 seconds
