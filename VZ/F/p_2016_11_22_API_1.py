# -*- coding: utf-8 -*-
import requests
from datetime import datetime

s_city = "Тернопіль"
city_id = 0
appid = "1bb8b7a186b957c05745fd9c421fd44c"


 # print('#'* 50)
'''
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'uk', 'APPID': appid})
    data = res.json()
    print("Характеристики погоди, атмосферні явища:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass
print('/' * 40)
'''
city_id = 691650
dict1 = dict()
str_api = ''
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'uk', 'APPID': appid})
    dict2 = dict()
    ls1 = []
    data = res.json()
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        str_api += '{0} {1:+3.0f} {2}\n'.format(i['dt_txt'], (i['main']['temp']), i['weather'][0]['description'])
        dict1[i['dt_txt']] = i['main']['temp']
        dat1 = i['dt_txt'].split(' ')
        dat1 = dat1[0]
        print(dat1)

        if dat1 in ls1:
            dict2[dat1].append(i['main']['temp'])
        else:
            ls1.append(dat1)
            dict2[dat1] = [i['main']['temp']]

except Exception as e:
    print("Exception (forecast):", e)
    pass
print(dict1)
print('-' * 50)
print(ls1)
print(str_api)

