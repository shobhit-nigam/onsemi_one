# try except
# multiple except blocks
# fails if we enter a string
# generic except block (catch all)
# name error

varx = 10
vary = 5
varz = 20
lista = [37, 28, 11, 13, 55, 16]



try:
    vara = varx/varz
    print(vara)
    i = int(input("enter the index:\n"))
    print(listb[i])
except ZeroDivisionError:
    print("we went wrong with denominator")
except IndexError:
    print("default index is 0")
    print("value =", lista[0])
    
print("application continues")



