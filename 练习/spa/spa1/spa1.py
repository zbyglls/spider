import requests
import os

'''
https://spa1.scrape.center/api/movie/?limit=10&offset=0
https://spa1.scrape.center/api/movie/?limit=10&offset=10
https://spa1.scrape.center/api/movie/1/
https://spa1.scrape.center/api/movie/2/
'''


def get_message(url):
    rsp = requests.get(url)
    res = rsp.json()
    movie_title = res['name'] + res['alias']
    img_src = [res['cover']]
    dir_name = make_dir(movie_title.replace(':', ''))
    save_pic(img_src, movie_title, dir_name)
    label = res['categories']
    regions = ''.join(res['regions']) + '/' + str(res['minute']) + '分钟'
    published_time = res['published_at']
    drama = res['drama']
    score = res['score']
    directors_name = [_['name'] for _ in res['directors']]
    directors_url = [_['image'] for _ in res['directors']]
    save_pic(directors_url, directors_name, dir_name)
    actors_name0 = [_['name'] for _ in res['actors']]
    actors_name1 = [_['role'] for _ in res['actors']]
    actors_name = [_[0] + '饰：' + _[1] for _ in zip(actors_name0, actors_name1)]
    actors_url = [_['image'] for _ in res['actors']]
    save_pic(actors_url, actors_name, dir_name)
    photo_url = res['photos']
    photos_name = [_ for _ in range(len(photo_url))]
    save_pic(photo_url, photos_name, dir_name)
    # movie_title, label, regions, drama, score, published_time 待用


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
    url = 'https://spa1.scrape.center'
    page = ['/api/movie/' + str(_) for _ in range(1, 101)]
    for _ in page:
        page_url = url + _
        get_message(page_url)
