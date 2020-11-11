import json

#json reading

fa = open("example_2.json", "r")

stra = json.load(fa)
#  converts it into a dictionary

fa.close()


# dont execute this:
def funca():
    print("hi")
    funca()
