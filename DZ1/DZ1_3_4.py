# -*- coding: utf-8 -*-
# 4. Видалення сусідів

list1 = [1, 1, 2, 2, 3, 4, 4, 1]
tumbler = 0
listnew = []
ch = 0
for i in list1:
    if tumbler == 0:
        listnew.append(i)
        tumbler = 1
        ch = i
    else:
        if i != ch:
            listnew.append(i)
            ch = i

print(listnew)
