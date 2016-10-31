# -*- coding: utf-8 -*-
# 7. Реверс стрічки

s = '12345'

s1 = s[::-1]
print(s1)

l = list(s)
l.reverse()
s2 = ''.join(l)
print(s2)

