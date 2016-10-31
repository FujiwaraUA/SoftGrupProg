# -*- coding: utf-8 -*-
# 10. Впорядкована підстрічка

s = 'abcsfsf'

s_dov = ''

for i in range(len(s)):
    for j in range(len(s), 0, -1):
        l1 = list(s[i:j])
        l1.sort()
        s1 = ''.join(l1)
        if s1 == s[i:j]:
            if len(s_dov) < len(s1):
                s_dov = s1
print(s_dov)