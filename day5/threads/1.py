#

import time

def funca():
    for i in range(3, 0, -1):
        print(f"task A finishes in {i} seconds")
        time.sleep(1)

def funcb():
    for i in range(9, 0, -1):
        print(f"task B finishes in {i} seconds")
        time.sleep(1)

def application():
    funca()
    funcb()
    for i in range(6, 0, -1):
        print(f"app finishes in {i} seconds")
        time.sleep(1)

application()
        
