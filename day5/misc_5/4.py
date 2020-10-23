# old string formats
# f strings

def funca(la):
    return la.upper()

dictx = {1:'hi', 2:'hello', 'xxx':'triple x'}

place = "hyderabad"
name = "nigam"
age = 40
statement = f"i am {funca(name)} and i live in {funca(place)} and am {age} years old"
statement_2 = f"one is {dictx[1]}, and {dictx['xxx']}"

print(statement)
print(statement_2)



def funca():
    for i in range(3, 0, -1):
        print("task a finishes")
