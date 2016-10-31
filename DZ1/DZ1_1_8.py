# -*- coding: utf-8 -*-
# 8. Підрахунок голосних

s = 'прпрпааАроААе'
golosni = ['а', 'е', 'и', 'і', 'о', 'у', 'є', 'ю', 'я', 'ї']
kilk = 0
for i in s.lower():
    if i in golosni:
        kilk += 1
print(kilk)
