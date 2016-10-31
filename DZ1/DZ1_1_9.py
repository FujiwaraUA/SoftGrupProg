# -*- coding: utf-8 -*-
# 9. Підрахунок входження підстрічки

s = 'wowowxcvxcvqwowcxvqowow'
kilk = 0

for i in range(len(s)):
    if s[i:i + 3] == 'wow':
        kilk += 1
print(kilk)
