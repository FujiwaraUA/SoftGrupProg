# -*- coding: utf-8 -*-
import requests

l = [31, 999, 1024, 502]
l1 = []
for i in l:
    domen = 'http://numbersapi.com/{}/math'.format(i)
    print(domen)
    res = requests.get(domen, params={'json': 'true'})
    print(res.json())
    data = res.json()
    if data['found']:
        l1.append('Interesting')
    else:
        l1.append('Boring')

print(l1)
