import requests
import json
import math

'''
抓取腾讯招聘信息

'''

def getResponse(page):
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10'.format(page)
    '''
    参数：
        timestamp：时间戳  # a =int(time.time() * 1000)
        countryId：国家
        cityId：城市
        bgIds=事业群
        productId
        categoryId
        parentCategoryId
        attrId
        keyword
        language：语言
        area：地区
    '''
    rsp = requests.get(url)
    rst = json.loads(rsp.text)['Data']['Posts']
    postIdlist = [_['PostId'] for _ in rst]
    return postIdlist


def getInfo(postIdlist):
    urls = ['https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}'.format(postId) for postId in postIdlist]
    for url in urls:
        rsp = requests.get(url)
        rst = json.loads(rsp.text)
        print(rst['Data']['RecruitPostName'])
        print(rst['Data']['BGName'],rst['Data']['LocationName'],rst['Data']['CategoryName'],rst['Data']['LastUpdateTime'])
        print('工作职责:')
        print(rst['Data']['Responsibility'])
        print('工作要求:')
        print(rst['Data']['Requirement'])

    return None

def getPages():
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=10'
    rsp = requests.get(url)
    rst = json.loads(rsp.text)['Data']['Count']
    pages = math.ceil(rst / 10)
    return pages


if __name__ == '__main__':
    pages = getPages()
    for page in range(pages):
        postIdlist = getResponse(page)
        getInfo(postIdlist)

