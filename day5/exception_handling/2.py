# try except
#
varx = 10
vary = 5
varz = 20
lista = [37, 28, 11, 13, 55, 16]



try:
    vara = varx/varz
    print(vara)
    i = int(input("enter the index:\n"))
    print(lista[i])
except ZeroDivisionError:
    print("we went wrong with denominator")
    
print("application continues")



