# map

nums_a = [5, 8, 2, 5, 9, 1, 4, 7, 10, 6]
nums_b = [7, 6, 8, 9, 3, 4, 1, 2, 5, 10]

def square(la):
    return la**2


listb = list(map(square , nums_a))

print(listb)
