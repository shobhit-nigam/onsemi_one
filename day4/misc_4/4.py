# map

nums_a = [5, 8, 2, 5, 9, 1, 4, 7, 10, 6]
nums_b = [7.2, 6, 8.2, 9, 3, 4, 1, 2, 5, 10, 23, 45]

def mul(la, lb):
    return la*lb


listb = list(map(mul , nums_a, nums_b))

print(listb)

varx = ''
print(type(varx))

varx = 0
print(type(varx))

varx = None
print(type(varx))
