# -*- coding: utf-8 -*-
# 5. Хороший

s = 'Цей комп’ютер не такий вже поганий!'

index_ne = s.find('не')
index_poganii = s.find('поганий')

if index_ne < index_poganii:
    print(s[:index_ne] + 'хороший' + s[index_poganii + 7:])
else:
    print(s)
