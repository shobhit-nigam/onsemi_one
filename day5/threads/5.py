# threads
# join
# shared resource with locks

import time
import threading

lk = threading.Lock()
ga = 0

def funca():
    global ga
    global lk
    lk.acquire()
    print(f"ga = {ga} in task a\n")
    for i in range(10):
        time.sleep(1)
    ga = ga+1
    print(f"ga = {ga} in task a\n")
    lk.release()
    
def funcb():
    global ga
    global lk
    lk.acquire()
    print(f"ga = {ga} in task b\n")
    for i in range(10):
        time.sleep(1)
    ga = ga+1
    print(f"ga = {ga} in task b\n")
    lk.release()

def application():
    ta = threading.Thread(target=funca)
    tb = threading.Thread(target=funcb)
    ta.start()
    tb.start()
    ta.join()
    tb.join()

    print("last line")


application()
        
