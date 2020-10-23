# old string formats
import time

place = "hyderabad"
name = "nigam"
age = 40

print("i am", name, "and i live in", place, "and am", age, "years old")

print("i am {} and i live in {} and am {} years old".format(name, place, age))

print("i am %s and i live in %s and am %d years old" %(name, place, age))



def funca():
    for i in range(3, 0, -1):
        print("task a finishes")
