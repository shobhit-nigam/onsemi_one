# more complicated POST requests
# forms

import requests
import json

payload_dict = {'username':['Mr.Nigam@gmail.com', 'shobhit']}
payload_tuples = [('profession', 'consultant'), ('domain', 'data science')]
payload_json = json.dumps(payload_dict)
url = 'http://httpbin.org/post'

r1 = requests.post(url,json=payload_json)    
print(r1.text)
print("--------")
