import json

#json reading

fa = open("example_2.json", "r")

stra = json.load(fa)
#  converts it into a dictionary

fa.close()


def funca(d):
    for k, v in d.items():
#        print(k)
#        print("-----")
#        print(v)
#        print("-----")
        if type(v) is dict:
            funca(v)
        else:
            print(v)

funca(stra)
