# -*- coding: utf-8 -*-
# 3. Сортування за останнім числом

list1 = [[1, 7], [1, 3], [3, 4, 5], [2, 2]]


def sort_index(i):
    return i[-1]


list1.sort(key=sort_index)
print(list1)
