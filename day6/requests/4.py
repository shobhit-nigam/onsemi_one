# response content

import requests

dataload = {'key1':'value1', 'key2':'value2'}

vara = requests.get('https://google.com')

print(vara.text)
print(vara.encoding)



