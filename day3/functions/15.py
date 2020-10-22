# user defined functions
# variable number of arguments
# conventionally --> args
# conventionally --> kwargs

def funca(la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)
    return args[1]

# will work
x = funca("hi", 22, 33, 44, planet="earth", galaxy="milky way")
print("----")
print(x)

