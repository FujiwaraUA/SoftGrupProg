# -*- coding: utf-8 -*-
# 4. Змішування

a = 'dog'
b = 'dinner'
a, b = a[0] + b[1] + a[2:], b[0] + a[1] + b[2:]
print(a + ' ' + b)
