# OOP
# Object Oriented Programming
#

class unix:
    def __init__(self, a=0, b=0, c=0):
        print("hello from init")
        self.data = a
        self.datb = b
        self.datc = c

    def display(self):
        print("data =", self.data)
        print("datb =", self.datb)
        print("datc =", self.datc)


obja = unix(11, 22, 33)
objb = unix(44, 55, 66)


