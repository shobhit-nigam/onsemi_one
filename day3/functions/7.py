# user defined functions
# return
lista = [7, 8, 9, 10, 30]


def funca(la, lb=111, lc=222):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)

funca(100, 200, 300)

print("----")

funca(100, 200)

# error
# funca(100, 200, 300, 400)

print("----")
funca(999)

