# more complicated POST requests
# forms

import requests

payload_dict = {'username':['Mr.Nigam@gmail.com', 'shobhit']}
payload_tuples = [('profession', 'consultant'), ('domain', 'data science')]
url = 'http://httpbin.org/post'

r1 = requests.post(url, data=payload_tuples)    
print(r1.text)
print("--------")


r2 = requests.post(url, data=payload_dict)    
print(r2.text)
