# global & local

ga = 12   # global

print("outside ga =", ga)

def funca():
    la = 14 # local
    ga = 20 # local
    print("inside the func ga =", ga)
    print("inside the func la =", la)

funca()

print("outside ga =", ga)
