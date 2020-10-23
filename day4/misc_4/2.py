# memory

varx = 30
vary = 24
varz = 30
vara = 100

print("varx =", id(varx))
print("vary =",id(vary))
print("varz =",id(varz))
print("vara =",id(vara))

varx = 300
print("-----")

print("varx =", id(varx))
print("vary =",id(vary))
print("varz =",id(varz))
print("vara =",id(vara))
