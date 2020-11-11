import json

#json reading

fa = open("example_1.json", "r")

stra = json.load(fa)
#  converts it into a dictionary

fa.close()

print(stra)

