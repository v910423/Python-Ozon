import requests


# payload = {'text':'ozon', 'lr':213}
# r = requests.get('https://yandex.ru/search', params=payload)
# # print(r.text)
#
# print(r.text)

payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)

print(r.text)