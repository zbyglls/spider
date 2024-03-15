import requests
import base64
import json

url = 'https://login1.scrape.center/'
form = {
    'username': 'admin',
    'password': 'admin'
}
token = {'token': base64.b64encode(bytes(json.dumps(form), encoding='utf-8')).decode('utf-8')}

print(token)

res = requests.post(url, data=token)


print(res.text)
