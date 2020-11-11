# headers

import requests

url = 'http://requestbin.net/'
head = {'user-agent':'my-app/0.0.1'}
 
vara = requests.get(url, headers=head)

