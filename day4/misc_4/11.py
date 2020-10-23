# filter

nums_a = [5, 8, 2, 5, 9, 1, 4, 7, 10, 6]
nums_b = [7.2, 6, 8.2, 9, 3, 4, 1, 2, 5, 10, 23, 45]
list_strings = ['w', 'o', 'r', 'l', 'd', ' ', 'p', 'e', 'a', 'c', 'e']
list_c = [99, None, '', False, [], {}, "great", 23.6, [5, 6, 7], 0]

def only_vowels(la):
    vowels = ['a', 'e', 'i', 'o', 'u', ' ']
    if la in vowels:
        return False
    else:
        return True

print(list_c)

listb = list(filter(None , list_c))

print(listb)


