# filter

nums_a = [5, 8, 2, 5, 9, 1, 4, 7, 10, 6]
nums_b = [7.2, 6, 8.2, 9, 3, 4, 1, 2, 5, 10, 23, 45]

def even(la):
    if la%2==0:
        return True
    else:
        return False

listb = list(filter(even , nums_b))

print(listb)


