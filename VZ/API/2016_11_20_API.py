# -*- coding: utf-8 -*-
# from urllib.request import urlretrieve
# import vk, os, time, math
#
# login = ''
# password = ''
#
# vkapi = vk.API('4567667', login, password)
#

import requests

for i in range(1000, 1010):
    parametru = {'fields': 'followers_count', 'user_ids': i}
    r = requests.get('https://api.vk.com/method/users.get', params=parametru)
    d1 = r.json()['response'][0]
    print('Прізвище: {} '.format(d1['last_name']))
    # print(d1)
    # print(type(r.json()))
    # print('*' * 30)
    # print(type(r))
