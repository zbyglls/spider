import requests


'''
https://spa1.scrape.center/api/movie/?limit=10&offset=0
https://spa1.scrape.center/api/movie/?limit=10&offset=10
https://spa1.scrape.center/api/movie/1/
https://spa1.scrape.center/api/movie/2/
'''
url = 'https://spa1.scrape.center/api/movie/?limit=10&offset=0'
rsp = requests.get(url)
a = rsp.json()
print(rsp.json())