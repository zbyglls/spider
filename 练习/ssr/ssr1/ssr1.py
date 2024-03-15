import os
import requests
from lxml import etree


def get_detail(url):
    rsp = requests.get(url)
    content = rsp.content
    html = etree.HTML(content)
    detail_list = html.xpath('//div[@class="el-card__body"]/div[@class="el-row"]/div[2]/a')
    detail = [_.attrib['href'] for _ in detail_list]
    return detail


def get_message(url, detail):
    for _ in detail:
        rsp = requests.get(url + _)
        content = rsp.content
        html = etree.HTML(content)
        img_src = [_.attrib['src'] for _ in html.xpath('//div[@class="item el-row"]/div/a/img')]
        movie_title = [_.text for _ in html.xpath('//div[@class="item el-row"]/div[2]/a/h2')]
        dir_name = make_dir(movie_title[0].replace(':', ''))
        save_pic(img_src, movie_title, dir_name)
        label = [_.text for _ in html.xpath('//div[@class="categories"]/button/span')]
        country = [_.text for _ in html.xpath('//div[@class="m-v-sm info"]/span')]
        country = ''.join(country)
        drama = html.xpath('//div[@class="drama"]/p')[0].text
        score = html.xpath('//div[@class="item el-row"]/div[3]/p[1]')[0].text
        director_url = [_.attrib['src'] for _ in html.xpath('//div[@class="directors el-row"]/div/div/div/img')]
        director_name = [_.text.replace('"', '') for _ in html.xpath('//div[@class="directors el-row"]/div/div/div/p')]
        save_pic(director_url, director_name, dir_name)
        actors_src = [_.attrib['src'] for _ in html.xpath('//div[@class="actors el-row"]/div/div/div/img')]
        actors_name0 = [_.text.replace('"', '') for _ in html.xpath('//div[@class="actors el-row"]/div/div/div/p[1]')]
        actors_name1 = [_.text.replace('"', '') for _ in html.xpath('//div[@class="actors el-row"]/div/div/div/p[2]')]
        actors_name = [_[0] + _[1] for _ in zip(actors_name0, actors_name1)]
        save_pic(actors_src, actors_name, dir_name)
        photos_src = [_.attrib['src'] for _ in html.xpath('//div[@class="photos el-row"]/div/div/div/div/img')]
        photos_name = [_ for _ in range(len(photos_src))]
        save_pic(photos_src, photos_name, dir_name)

        # movie_title, label, country, drama, score 待用


def save_pic(pic_url, pic_name, dir_name):
    for _ in zip(pic_url, pic_name):
        rsp = requests.get(_[0])
        with open('./{}/{}.png'.format(dir_name, _[1]), 'wb') as file:
            file.write(rsp.content)

    return None


def make_dir(name):
    os.mkdir(name)

    return name


if __name__ == '__main__':
    url = 'https://ssr1.scrape.center'
    page = ['/page/' + str(_) for _ in range(1, 11)]
    for _ in page:
        page_url = url + _
        detail = get_detail(page_url)
        get_message(url, detail)
