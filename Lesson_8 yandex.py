from bs4 import BeautifulSoup
import requests

payload = {'text':'ozon', 'lr':159}
result = requests.get('https://yandex.ru/search/', params=payload).text

soup = BeautifulSoup(result, 'html.parser')

print(soup.prettify())

referals = open('referals.txt', 'a')
for link in soup.find_all('a'):
    referals.write(link.get('href')+'\n')