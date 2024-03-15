import requests
from lxml import etree


'''
https://spa4.scrape.center/
https://spa4.scrape.center/api/news/?limit=10&offset=0


thumb: "http://n.sinaimg.cn/spider20201021/214/w700h314/20201021/2308-kavypmp7803186.png"
title: "澳门将同期举办3个经贸展会 发挥叠加效应促合作"
updated_at: "2020-10-20T17:30:16.274131Z"
url: "https://news.sina.com.cn/c/2020-10-21/doc-iiznctkc6705317.shtml"
website: "新浪新闻"
'''

def get_list(url):
    res = requests.get(url)
    return res.json()['results']


def get_source(data):
    urls = []
    for _ in data:
        urls.append(_['url'])
    return urls


def get_detail(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    title = html.xpath('//h1[@class="main-title"]/text()')[0]
    print(title)
    article = html.xpath('//p[@cms-style="font-L"]/text()')
    print(article)


if __name__ == '__main__':
    url = 'https://spa4.scrape.center/api/news/?limit=10&offset=0'
    res = get_list(url)
    urls = get_source(res)
    get_detail(urls[0])