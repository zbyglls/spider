import requests
from lxml import etree
'''
抓取糗事百科段子内容

'''

url = 'https://www.qiushibaike.com/text/'
'''
抓取所有页直接在url后添加
page/页数
'''
rsp = requests.get(url )
html = rsp.text

html = etree.HTML(html)

# 使用xpath匹配每条段子内容
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')[0]

# 匹配作者
author = rst.xpath('//div[@class="author clearfix"]/a[2]/h2/text()')
#author = [_.strip() for _ in author]

# 匹配段子主要内容
text = rst.xpath('//div[@class="content"]/span/text()')
#text = [_.strip() for _ in text]
article = dict(zip(author,text))

for k,v in article.items():
    print(k,'-----',v)
