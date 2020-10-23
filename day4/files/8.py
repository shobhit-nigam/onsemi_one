# files
# read all lines as a list
# 

name = 'data.txt'
fa = open(name, 'r')
stra = fa.read()
lista = stra.splitlines()
print(lista)

lista = stra.split()
print(lista)

fa.close()
