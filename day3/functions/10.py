# user defined functions
# return
lista = [7, 8, 9, 10, 30]

# error prone
def funca(la=333, lb=111, lc=222):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)

funca(100)
print("----")

funca(lb=100)
print("----")

funca(lb=100, lc=200, la=300)
print("----")

