# user defined functions
# variable number of arguments

# error prone
def funca(la, lb, *lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


funca(11, 22, 33, 44, 55)
print("----")

