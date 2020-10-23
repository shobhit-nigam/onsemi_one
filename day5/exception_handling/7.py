# try except
# multiple except blocks
# nesting of excepts

varx = 10
vary = 5
varz = 20
lista = [37, 28, 11, 13, 55, 16]



try:
    vara = varx/varz
    print(vara)
    try:
        i = int(input("enter the index:\n"))
        print(listb[i])
    except NameError:
        print("you got the name wrong")
except ZeroDivisionError:
    print("we went wrong with denominator")
except IndexError:
    print("default index is 0")
    print("value =", lista[0])
    
print("application continues")



