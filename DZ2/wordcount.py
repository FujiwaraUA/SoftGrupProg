""" "Кількість слів"

Функція main() нижче вже визначена і заповнена. Вона викликає функції 
print_words() і print_top(), які вам потрібно заповнити.

1. Якщо при виклику файлу задано прапорець --count, викликається функція 
print_words(filename), яка підраховує, як часто кожне слово зустрічається 
в тексті і виводить:
слово1 кількість1
слово2 кількість2
...

Виведений список відсортуйте за алфавітом. Зберігайте всі слова 
в нижньому регістрі, тобто слова "Слон" і "слон" будуть оброблятися як одне 
слово.

2. Якщо задано прапорець --topcount, викликається функція print_top(filename),
яка аналогічна функції print_words(), але виводить тільки топ-20 слів, які 
найбільш часто зустрічаються, таким чином першим буде слово, яке саме частіше
зустрічається, за ним наступне за частотою і т.д.

Використовуйте str.split() (без аргументів), щоб розбити текст на слова.

Відсікайте знаки пунктуації за допомогою str.strip() з знаками пунктуації 
в якості аргументу.

Не пишіть всю програму відразу. Доведіть її до якогось проміжного 
стану і виведіть вашу поточну структуру даних. Коли все буде працювати 
як потрібно, перейдіть до наступного етапу.

Визначіть додаткову функцію, щоб уникнути дублювання 
коду в середині print_words() і print_top().

"""

import sys
import string

def rid_slovnik(filename):
    file = open(filename, encoding='utf-8')
    s1 = file.read()
    file.close()
    s1 = s1.lower()
    l1 = s1.split()
    for i in range(len(l1)):
        l1[i] = l1[i].strip(string.punctuation + ' ')
    slovnik1 = {}
    for i in l1:
        if i in slovnik1:
            slovnik1[i] = slovnik1[i] + 1
        else:
            slovnik1[i] = 1
    if '' in slovnik1:
        del slovnik1['']
    return slovnik1

def print_words(filename):
    slovnik2 = rid_slovnik(filename)
    l2 = [(key, value) for key, value in slovnik2.items()]
    l2.sort()
    for i in l2:
        print(i[0], i[1])



def print_top(filename):
    slovnik2 = rid_slovnik(filename)
    l2 = [( value, key,) for key, value in slovnik2.items()]
    l2.sort(reverse=True)
    for i in range(20):
        print(l2[i][1], l2[i][0])

# +++ваш код+++
# Визначте і заповніть функції print_words(filename) і print_top(filename).
# Ви також можете написати додаткову функцію, яка читає файл,
# будує за ним словник слово/кількість і повертає цей словник.
# Потім print_words() і print_top() зможуть просто викликати цю допоміжну функцію.

###

# Це базовий код для розбору аргументів командної стрічки.
# Він викликає print_words() і print_top(), які необхідно визначити.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
