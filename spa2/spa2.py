import time
import hashlib
import base64
import requests


'''
https://spa1.scrape.center/api/movie/?limit=10&offset=0
https://spa1.scrape.center/api/movie/?limit=10&offset=10
https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=MTljYzAxOWM4NTRjZmIyNGZmMzU2MmM2NmMwZGYwY2E0ZjYyNWIxMCwxNzA2NTEwMjcw
https://spa2.scrape.center/api/movie/?limit=10&offset=10&token=MDQ3MjhlM2Q3YzI4MGM5ZjQ1ZjA1ZTUyMDE3ZDFmZGY1ZWFjMTg3NSwxNzA2NTEwMzIz
https://spa1.scrape.center/api/movie/1
https://spa1.scrape.center/api/movie/2
https://spa2.scrape.center/api/movie/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx/?token=ODY0YjY0ODg3NGM5NTFiNGYyYTQxNDM3M2VlYzg3OGRlYjNkY2Q2ZCwxNzA2NTEwMDUx
https://spa2.scrape.center/api/movie/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIy/?token=MzY4ZWFkNDM4MTkwMTA0YTk5MTZlMzNjNzY2NDIyNjNkYmI4NjNkMiwxNzA2NTA5ODQ1
https://spa2.scrape.center/api/movie/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx/?token=NDM4NzRjMWU0YTNhMDQzZDUxMDgwZGE1NGIzNWI3YTQzZDhhNjczYywxNzA2Nzc4ODg4
'''

LIMIT = 10
PAGE = 1
SECRET='ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
offset = (PAGE - 1) * 10


def get_token(args):
    timestep = str(time.time())[:10]
    args.append(timestep)
    sign = hashlib.sha1(','.join(args).encode()).hexdigest()
    return base64.b64encode(bytes(','.join([sign,timestep]),encoding='utf-8')).decode('utf-8')


args = ['/api/movie', str(offset)]
token = get_token(args)
index_url = f'https://spa2.scrape.center/api/movie/?limit={LIMIT}&offset={offset}&token={token}'
res = requests.get(index_url)
id = [_['id'] for _ in res.json()['results']]

for _ in id:
    key = base64.b64encode(bytes(SECRET + str(_), encoding='utf-8')).decode('utf-8')
    args = [f'/api/movie/{key}', str(offset)]
    token = get_token(args)
    detail_url = f'https://spa2.scrape.center/api/movie/{key}?token={token}'
    print(detail_url)
    res = requests.get(detail_url)
    print(res.json())


