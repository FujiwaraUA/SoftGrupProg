# -*- coding: utf-8 -*-
# 1. Початок і кінець співпадають

list1 = ['ww', 'wsdfw', 's', 'sds']
kil = 0

for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        kil += 1
print(kil)
