import requests
from bs4 import BeautifulSoup
import re
import os
import urllib

path = os.getcwd() #печать текущей директории
print(path)
URL = input('enter site address: ') #http://www.ya.ru
folder = input('enter name of folder: ')
while True:
    try:
        os.mkdir(folder)
    except:
        print('already exist')
        folder = input('enter other name: ')
    else:
        break


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('img', src=re.compile('\/[a-z\-\d\/]+.jpg'))
print(results)

arr=[]
for i in range(0, len(results)):
    arr.append(results[i]['src'])
    img_data = requests.get(URL + arr[i]).content
    handler = open(folder+'/'+str(i)+'.jpg', 'wb')
    handler.write(img_data)
    handler.close()




# site = open('index.html')
# content = site.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# print(soup.title.string)
# print(soup.find_all('p'))