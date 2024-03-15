import requests





'''
https://spa3.scrape.center/api/movie/?limit=10&offset=0
https://spa3.scrape.center/api/movie/?limit=10&offset=10

url = f'https://spa3.scrape.center/api/movie/?limit=10&offset={offset}'
'''



def get_respone(offset, limit=10):
    url = f'https://spa3.scrape.center/api/movie/?limit={limit}]&offset={offset}'
    res = requests.get(url)
    return res.json()['results']


def get_detail(data):
    for _ in data:
        pass