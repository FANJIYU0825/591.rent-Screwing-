import requests as re

url = 'https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1'

res=re.get(url)

print(f'status_code:{res.status_code}')
