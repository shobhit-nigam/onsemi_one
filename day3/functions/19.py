# global & local

ga = 12   # global

print("outside ga =", ga)

def funca():
    print("inside the func ga =", ga)
    la = 14   # local
    print("inside the func la =", la)

funca()

#error
print("outside la =", la)
