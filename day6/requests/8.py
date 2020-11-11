# more complicated POST requests
# forms

import requests

url = 'http://httpbin.org/post'

#before payload:
r1 = requests.post(url)    
print(r1.text)
print("--------")

#before payload:
payload = {'username':'Mr.Nigam@gmail.com', 'password':'mrs.nigam'}
r1 = requests.post(url, payload)    
print(r1.text)
