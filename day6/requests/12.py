# errors & exceptions

import requests



r1 = requests.post('https://google.com/')
r1.raise_for_status()
