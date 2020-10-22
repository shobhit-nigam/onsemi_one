# user defined functions
# return
lista = [7, 8, 9, 10, 30]


def calculator(la, e):
    temp = []
    for val in la:
        temp.append(val**e)

    return temp


print(calculator([11, 22, 33], 2))
