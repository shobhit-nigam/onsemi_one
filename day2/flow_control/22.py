# flow control
# in , not in 

lista = ['london', 'shanghai', 'cairo', 'moscow', 'dhaka', 'madrid', 'kuala lumpur']
listb = ['lagos', 'manila', 'london', 'austin', 'melbourne', 'madrid', 'mumbai', 'oslo']

common = []

for val in lista:
    if val in listb:
        common.append(val)
    

