# -*- coding: utf-8 -*-
import requests
from datetime import datetime

s_city = "Тернопіль"
city_id = 0
appid = "1bb8b7a186b957c05745fd9c421fd44c"
'''
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'lang': 'uk', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass
'''
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
        # print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        str_api += '{0} {1:+3.0f} {2}\n'.format(i['dt_txt'], (i['main']['temp']), i['weather'][0]['description'])
        dict1[i['dt_txt']] = i['main']['temp']
        dat1 = i['dt_txt'].split(' ')
        dat1 = dat1[0]
        # print(dat1)

        if dat1 in ls1:
            dict2[dat1].append(i['main']['temp'])
        else:
            ls1.append(dat1)
            dict2[dat1] = [i['main']['temp']]

except Exception as e:
    print("Exception (forecast):", e)
    pass
# print(dict1)
# print('-' * 50)
# print(ls1)
# print(dict2)
dict3 = dict()

for ind, i in enumerate(ls1):
    # print(i)
    # print(ind)
    # print(dict2[i])
    if len(dict2[i]) == 8:
        dict3[i] = {}
        dict3[i]['Вночі'] = '{0:+.0f}   {1:+.0f}'.format(min(dict2[i][0:3]), max(dict2[i][0:3]))
        dict3[i]['Вранці'] = '{0:+.0f}   {1:+.0f}'.format(min(dict2[i][2:5]), max(dict2[i][2:5]))
        dict3[i]['Вдень'] = '{0:+.0f}   {1:+.0f}'.format(min(dict2[i][4:7]), max(dict2[i][4:7]))
        dict3[i]['Увечері'] = '{0:+.0f}   {1:+.0f}'.format(min(dict2[i][6:]), max(dict2[i][6:]))

# print(dict3)
