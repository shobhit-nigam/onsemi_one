import json

#json reading

fa = open("example_2.json", "r")

stra = json.load(fa)
#  converts it into a dictionary

fa.close()

print(stra)

print(stra['quiz']['maths']['q1']['answer'])
