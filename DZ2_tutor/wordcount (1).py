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
import codecs
import string

# +++ваш код+++
# Визначте і заповніть функції print_words(filename) і print_top(filename).
# Ви також можете написати додаткову функцію, яка читає файл,
# будує за ним словник слово/кількість і повертає цей словник.
# Потім print_words() і print_top() зможуть просто викликати цю допоміжну функцію.

###

def get_words_dict(filename):

    f = codecs.open(filename, encoding='utf-8')
    word_list = f.read().split()

    word_dict = {}
    string_for_strip = string.punctuation + ' '
    for word in word_list:
        word = word.strip(string_for_strip).lower()
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def print_words(filename):
    word_dict = get_words_dict(filename)

    for k in sorted(word_dict.keys()):
        print('{0:20} {1:5}'.format(k, word_dict[k]))

def print_top(filename):
    word_dict = get_words_dict(filename)

    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print('{0:20} {1:5}'.format(k, v))


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
