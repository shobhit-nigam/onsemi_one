# OOP
# Object Oriented Programming
#

class unix:

    def display(self):
        print("data =", self.data)
        print("datb =", self._datb)
        print("datc =", self.__datc)
        print("datd =", self.__datd__)

    def __init__(self, a=0, b=0, c=0, d=0):
        print("hello from init")
        self.data = a
        self._datb = b
        self.__datc = c
        self.__datd__ = d


obja = unix(11, 22, 33, 100)
objb = unix(44, 55, 66, 77)

#  instantiation 


