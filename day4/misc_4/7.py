# types, dynamism

print(type(print))

print("hello")

display = print

print = 23

display("hi")
display(print)
