# -*- coding: utf-8 -*-
import requests
# print ("downloading with requests")
# url = 'https://pogoda.yandex.ru/static/cities.xml'
# r = requests.get(url)
# with open("cities.xml", "wb") as code:
#     code.write(r.content)

# url1 = 'http://export.yandex.ru/weather-ng/forecasts/33415.xml'
# r1 = requests.get(url1)
# with open('33415.xml', 'wb') as code:
#     code.write(r1.content)
parametru = {'q': 'London'}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parametru)
d1 = r.json()
print(d1)
# print(type(r.json()))
# print('*' * 30)
# print(type(r))

