# -*- coding: utf-8 -*-
# 12. A & B

a = 12
b = 11

if type(a) == str or type(b) == str:
    print('отримана стрічка')
elif a > b:
    print('більше')
elif a == b:
    print('рівні')
elif a < b:
    print('менше')