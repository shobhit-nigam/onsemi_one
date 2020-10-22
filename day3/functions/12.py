# user defined functions
# variable number of arguments
# conventionally --> args

def funca(la, lb, *args, ld):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)

# runtime aerror: 
funca(11, 22, 33, 44, 55)
print("----")

