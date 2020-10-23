# types, dynamism

print(type(print))

print("hello")

display = print

print = 23

display("hi")
display(print)

#
#def print(la):
#    f = open("", "w")
#    f.write(la)


