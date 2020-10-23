# OOP
# Object Oriented Programming

class employee:
    eid = 0
    name = "john doe"
    dept = None

    def update(self, e, n, d):
        self.eid = e
        self.name = n
        self.dept = d

    def display(self):
        print("welcome", self.name, "your dept is", self.dept)


obja = employee()
objb = employee()
