# lambda , map

nums_a = [5, 8, 2, 5, 9, 1, 4, 7, 10, 6]
nums_b = [7, 6, 8.2, 9, 3, 4, 1, 2, 5, 10, 23, 45]


listb = list(map(lambda x, y : x+y , nums_a, nums_b))

print(listb)

listb = list(filter(lambda x: x%2==0, nums_b))

print(listb)

listb = list(map(lambda x, y : x if x>y else y , nums_a, nums_b))

print(listb)


