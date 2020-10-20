# dictionary
# nesting

fruits = {'general':'apples', 'citrus':('oranges', 'limes'), 'berry':['straberries', 'kiwifruit'], 'melons':'watermelons'}

vegan = {'tubers':['potatoes','yam'], 'leafy':'lettuce', 'fruits':fruits}

print("vegan =", vegan)
print("----")

print(vegan['fruits']['berry'][1][2])
