import time
import requests

url = "https://ssr4.scrape.center/"
page = ['page/' + str(_) for _ in range(1, 11)]
page_url = [url + _ for _ in page]
for _ in page_url:
    rsp = requests.get(_)
    time.sleep(5)
    # 响应增加了 5 秒延迟，测试慢速网站爬取或做爬取速度测试，减少网速干扰。
    with open('{}.html'.format(_[-1]), 'wb') as f:
        f.write(rsp.content)


# 取数据同ssr1.py
