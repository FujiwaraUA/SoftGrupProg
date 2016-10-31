# -*- coding: utf-8 -*-
# 6. Дві половинки

a = '01234'
b = '56789'
dov_a = len(a)
dov_b = len(b)
dov_a2 = dov_a // 2
dov_b2 = dov_b // 2

if (dov_a % 2) == 0:
    if (dov_b % 2) == 0:
        print(a[:dov_a2] + b[:dov_b2] + a[dov_a2:] + b[dov_b2:])
    else:
        print(a[:dov_a2] + b[:dov_b2 + 1] + a[dov_a2:] + b[dov_b2 + 1:])
else:
    if (dov_b % 2) == 0:
        print(a[:dov_a2 + 1] + b[:dov_b2] + a[dov_a2 + 1:] + b[dov_b2:])
    else:
        print(a[:dov_a2 + 1] + b[:dov_b2 + 1] + a[dov_a2 + 1:] + b[dov_b2 + 1:])
