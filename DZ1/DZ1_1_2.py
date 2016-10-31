# -*- coding: utf-8 -*-
# 2. Обидва кінці

s = '12'

if len(s) > 1:
    print(s[:2] + s[-2:])
else:
    print('')

'''
# Якщо стрічка складається з 2 або 3 елементів, щоб елементи не повторювалися.
s = '123456'
dovgina = len(s)

if dovgina > 3:
    print(s[:2] + s[-2:])
elif dovgina == 3:
    print(s[:2] + s[-1])
elif dovgina == 2:
    print(s)
else:
    print('')
'''
