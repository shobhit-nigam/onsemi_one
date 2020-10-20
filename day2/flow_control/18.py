# flow control
# for, break

lista = ['london', 'shanghai', 'cairo', 'moscow', 'dhaka', 'madrid', 'kuala lumpur']

x = input("which city :")

for city in lista:
    if x == city:
        print("found it")
        break
else:
    print("not found")
    

