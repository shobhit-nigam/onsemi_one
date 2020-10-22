fruits = {'general':'apples', 'citrus':('oranges', 'limes'),
          'berry':['straberries', 'kiwifruit'], 'melons':'watermelons'}

vegan = {'tubers':['potatoes','yam'], 'leafy':'lettuce', 'fruits':fruits}


for x in fruits:
    print(x)

print("----")

for x in fruits.values():
    print(x)
   
print("----")

for x in fruits:
    print(fruits[x])


print("----")

for k, v in fruits.items():
    print(k, "\t", v)

