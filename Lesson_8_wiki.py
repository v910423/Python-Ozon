from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import datetime
import random
import requests

random.seed(datetime.datetime.now())


def getLinks(arcticleURL):
    html = requests.get(f'https://en.wikipedia.org{arcticleURL}').text
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Ozon.ru')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    print('https://en.wikipedia.org/'+newArticle)
    links = getLinks(newArticle)