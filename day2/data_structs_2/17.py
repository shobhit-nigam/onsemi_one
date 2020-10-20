# dictionary
# indexed using keys

fruits = {'general':'apples', 'citrus':('oranges', 'limes'), 'berry':['straberries', 'kiwifruit'], 'melons':'watermelons'}

print("fruits =", fruits)
print(type(fruits))

# error
# print(fruits[2])

print(fruits['citrus'])

fruits['berry'].append('passionfruit')
print((fruits))
