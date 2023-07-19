import requests

url = 'https://ssr1.scrape.center'
# verify=False 忽略ssl证书验证
requests.packages.urllib3.disable_warnings()  # 忽略ssl验证警告
rsp = requests.get(url, verify=False)

# 取数据同ssr1.py
