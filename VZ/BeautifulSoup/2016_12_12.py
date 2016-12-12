# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
ls = []
dict1 = dict()
url = 'https://yandex.ua/pogoda/region/20531'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
city_ls = soup.find_all('a', 'place-list__item-name')
for i in city_ls:
    ls.append(i.text)
    dict1[i.text] = i['href'].split('/')[2]

print(ls)
print(dict1)