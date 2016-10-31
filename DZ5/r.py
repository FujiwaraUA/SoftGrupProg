#
"""
1. Написати просту програму для імітації роботи команди  Unix - grep.
(Програма командного рядка, вбудована в Unix називається grep
(Generalized Regular Expression Parser), що робить майже таке саме,
як приклади з search().)

Попросіть користувача ввести регулярний вираз і підрахувати кількість рядків,
які відповідають регулярному виразу:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$


2. Написати програму для пошуку рядків виду
"New Revision: 39772"
і витягти число з кожної з стрічок, використовуючи регулярний вираз
і метод findall().
Обчислити середнє значення чисел і роздрукувати середнє значення.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259

"""

import re


def task1():
    filename = input('Enter a file name: ')
    pattern = input('Enter a regular expression: ')
    fail1 = open(filename)
    n = 0

    for line in fail1:
        if re.search(pattern, line):
            n += 1
    print(' {0} had {1} lines that matched {2}'.format(filename, n, pattern))


def task2():
    filename = input('Enter a file name: ')
    fail1 = open(filename)
    l = []
    for line in fail1:
        i = re.findall('^New *Revision: *([0-9]*)', line)
        if i:
            l.append(int(i[0]))
    rez = sum(l) / len(l)
    print(rez)


task1()
task2()
