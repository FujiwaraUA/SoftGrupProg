# -*- coding: utf-8 -*-
import requests
s_city = "Тернопіль"
city_id = 0
appid = "1bb8b7a186b957c05745fd9c421fd44c"
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

print('#'* 50)
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
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'uk', 'APPID': appid})

    data = res.json()
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
except Exception as e:
    print("Exception (forecast):", e)
    pass

