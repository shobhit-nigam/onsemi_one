# threads
# join
# shared resource

import time
import threading

ga = 0

def funca():
    global ga
    print(f"ga = {ga} in task a\n")
    for i in range(10):
        time.sleep(1)
    ga = ga+1
    print(f"ga = {ga} in task a\n")
    
def funcb():
    global ga
    print(f"ga = {ga} in task b\n")
    for i in range(10):
        time.sleep(1)
    ga = ga+1
    print(f"ga = {ga} in task b\n")

def application():
    ta = threading.Thread(target=funca)
    tb = threading.Thread(target=funcb)
    ta.start()
    tb.start()
    ta.join()
    tb.join()

    print("last line")


application()
        
