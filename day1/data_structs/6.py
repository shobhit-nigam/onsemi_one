# lists
# mutable
# deleting functions

num_a = [8, 9, 3, 4, 6, 10, 20]
num_b = [33.4, 77.8, 99.0, 12.3]
south_america = ['lima', 'bogota', 'brasillia', 'buenos aires', 'santiago', 'caracas']
lista = [23, 88.9, 'hello', 'hi', 10]
listb = [22, 'tt', lista, 'yy']

print(south_america)
print("-----")

south_america.remove('santiago')
print(south_america)
print("-----")

south_america.pop(2)
print(south_america)
print("-----")

south_america.pop()
print(south_america)
print("-----")

south_america.clear()
print(south_america)
print("-----")
