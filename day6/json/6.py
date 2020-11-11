import json

#json writing

dictx = {'aa':12, 'bb':34, 'cc':678}

fa = open("example_3.json", "w")

json.dump(dictx, fa)
#  converts dictionary into a json file

fa.close()


dictx['aa']=13
