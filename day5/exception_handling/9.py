# try except
# multiple except blocks
# nesting of excepts
    # can be handled by outer except too

varx = 10
vary = 5
varz = 20
lista = [37, 28, 11, 13, 55, 16]

def funca(la):
    # some calculations
    try:
        avg = sum(la)/len(la)
        print("average =", avg)
    except TypeError:
        print("you don't have a list of numbers")

try:
    #funca(lista)
    funca([])
except ZeroDivisionError:
    print("we went wrong with denominator")
except IndexError:
    print("default index is 0")
    print("value =", lista[0])
    
print("application continues")


