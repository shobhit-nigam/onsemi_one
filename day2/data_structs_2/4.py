#list
# reference, copy
num_a = [8, 9, 3, 4, 6, 10, 20, 33, 11]
num_b = [33.4, 77.8, 99.0, 12.3]
south_america = ['Lima', 'Bogota', 'brasillia', 'buenos aires', 'Santiago', 'caracas']
lista = [23, 88.9, 'hello', 'hi', 10]
listb = [22, 'tt', lista, 'yy']

american_cities = ['phoenix', 'toronto', 'mexico city']
print(american_cities)
american_cities.append(south_america)
print(american_cities)      # list

print(american_cities[3])   # inner list

print(american_cities[3][1])  # string within the inner list

print(american_cities[3][1][2])  # character within the string within the inner list
