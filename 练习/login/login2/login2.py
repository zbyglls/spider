import requests


def get_cookie():
    url = 'https://login2.scrape.center/login?next=/'
    form = {
        'username': 'admin',
        'password': 'admin'
    }
    res = requests.post(url, data=form)
    return res.history[0].cookies


def main():
    url = 'https://login2.scrape.center/'
    cookie = get_cookie()
    print(cookie)
    res = requests.get(url, cookies=cookie)
    print(res.text)


if __name__ == '__main__':
    main()
