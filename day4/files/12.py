# files
# extrat a column

fa = open("info.txt", "r")
stra = fa.read()
fa.close()

lista = stra.splitlines()

col_list = []

for line in lista:
    temp = line.split()
    col_list.append(int(temp[1]))


print(col_list)
