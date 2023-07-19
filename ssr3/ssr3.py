import requests

url = 'https://ssr3.scrape.center/'
# HTTP basic Auth
# web客户端验证
auth = ('admin', 'admin')
rsp = requests.get(url, auth=auth)
# 取数据同ssr1.py
