import requests

dataload = {'key1':'value1', 'key2':'value2'}

vara = requests.get('https://httpbin.org/get', params=dataload)

print(vara)
print(vara.url)



