# -*- coding: utf-8 -*-
# 2. Ті, що починаються з X на початку

list1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
ch = 'x'
list2 = []
list3 = []
for i in list1:
    if i[0] == ch:
        list2.append(i)
    else:
        list3.append(i)

list2.sort()
list3.sort()
list2.extend(list3)
print(list2)
