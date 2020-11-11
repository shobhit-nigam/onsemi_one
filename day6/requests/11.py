# POST a multipart-encoded file
# forms

import requests
import json

'''
payload_dict = {'username':['Mr.Nigam@gmail.com', 'shobhit']}
payload_tuples = [('profession', 'consultant'), ('domain', 'data science')]
payload_json = json.dumps(payload_dict)
'''


files_data = {'upload_file':open("hi.txt", 'rb')}
url = 'http://httpbin.org/post'

r1 = requests.post(url,files=files_data)    
print(r1.text)
print("--------")
