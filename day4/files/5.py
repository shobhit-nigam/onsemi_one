# files
# read n num bytes (chars)
# tell 

name = 'data.txt'
fa = open(name, 'r')
stra = fa.read(5)
print(stra)

strb = fa.read(7)
print(strb)

print(fa.tell())
