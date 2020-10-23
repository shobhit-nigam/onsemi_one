# OOP
# Object Oriented Programming
# self -- not a keyword
#      -- convention

class employee:
    eid = 0
    name = "john doe"
    dept = None

    def update(self, e, n, d):
        self.eid = e
        self.name = n
        self.dept = d

    def display(ttt):
        print("welcome", ttt.name, "your dept is", ttt.dept)


obja = employee()
objb = employee()
