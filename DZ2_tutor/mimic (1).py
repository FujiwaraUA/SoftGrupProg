"""Імітація тексту

Прочитайте файл, вказаний в командній стрічці.
Використовуйте str.split() (без аргументів) для отримання всіх слів в файлі.
Замість того, щоб читати файл пострічково, простіше зчитати
його в одну велику стрічку і застосувати до неї split() один раз.

Створіть "імітаційний" словник, який зв’язує кожне слово
зі списком всіх слів, які безпосередньо слідують за цим словом в файлі.
Список слів може бути в довільному порядку і повинен включати дублікати. 

Так, наприклад, для тексту "Привіт, світ! Привіт, Всесвіт!" ми отримаємо такий
імітаційний словник:
{'': ['Привіт,'], 'Привіт,': ['світ!', 'Всесвіт!'], 'світ!': ['Привіт,']}
Будемо вважати, в якості ключа для першого слова в файлі використовується пуста
стрічка.

За допомогою імітаційного словника доволі просто генерувати випадкові тексти, 
які імітують оригінальний. Візьміть слово, перегляньте які слова можуть бути за ним, 
виберіть одне з них наугад, виведіть його і використовуйте це слово 
в наступній ітерації.

Використовуйте пусту стрічку в якості ключа для першого слова.
Якщо ви коли-небудь застрягнете на слові, якого немає в словнику,
повернітьсь до пустої стрічки, щоб продовжити генерацію тексту.

Стандартний python-модуль random включає в себе метод 
random.choice(list), який вибирає випадковий елемент із непустого списку.

"""

import random
import sys
import codecs


def mimic_dict(filename):
    """Повертає імітаційний словник, який співставляє кожне слово 
    зі списком слів, які безпосередньо слідують за ним в тексті"""
    # +++ваш код+++
    f = codecs.open(filename, encoding='utf-8')
    word_list = f.read().split()

    res = {}
    prev = ''

    for x in word_list:
        if prev in res:
            res[prev].append(x)
        else:
            res[prev] = [x, ]
        prev = x
    return res



def print_mimic(mimic_dict, word):
    """Приймає в якості аргументів імітаційний словник і початкове слово,
    виводить 200 випадкових слів, згідно правил імітації."""
    # +++ваш код+++
    res = []

    for i in range(200):
        if not word in mimic_dict:
            word = ''
        word = random.choice(mimic_dict[word])
        res.append(word)

    print(' '.join(res))



def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
