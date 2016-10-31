# -*- coding: utf-8 -*-
# 3. Крім першого

s = 'vavvsvas'

s = s[0] + s[1:].replace(s[0], '*')
print(s)
