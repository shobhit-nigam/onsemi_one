# response content

import requests

dataload = {'key1':'value1', 'key2':'value2'}

vara = requests.get('https://api.github.com/events')

print(vara.text)
print(vara.encoding)

# change the encoding

vara.encoding = 'ISO-8859-1'

fa = open("sample.txt", "wb")
fa.write(vara.content)
fa.close()

