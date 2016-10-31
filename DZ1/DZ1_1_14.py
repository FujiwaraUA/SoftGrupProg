# -*- coding: utf-8 -*-
# 14. Кожен третій

list1 = ['1', '2', '3', '4', '5', '6', '7']
list_new = []

for i in range(len(list1)):
    if (i + 1) % 3 == 0:
        list_new.append(list1[i])

print(list_new)
