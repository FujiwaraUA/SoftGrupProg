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


def mimic_dict(filename):
    """Повертає імітаційний словник, який співставляє кожне слово 
    зі списком слів, які безпосередньо слідують за ним в тексті"""
    # +++ваш код+++
    file = open(filename, encoding='utf-8')
    s1 = file.read()
    file.close()
    l1 = s1.split()
    imit_slovnik = {'':[l1[0]]}
    rele = 0
    for i in range(len(l1)):
        if rele != 0 and l1[i - 1] not in imit_slovnik:
            imit_slovnik[l1[i - 1]] = [l1[i]]
        elif rele != 0 and l1[i - 1] in imit_slovnik:
            imit_slovnik[l1[i - 1]] =imit_slovnik[l1[i - 1]] + [l1[i]]
        else:
            rele = 1
    return imit_slovnik


def print_mimic(mimic_dict, word):
    """Приймає в якості аргументів імітаційний словник і початкове слово,
    виводить 200 випадкових слів, згідно правил імітації."""
    # +++ваш код+++
    kluch = word
    for i in range(200):
        if kluch in mimic_dict:
            kluch = random.choice(mimic_dict[kluch])
            print(kluch)
        else:
            kluch = word
            kluch = random.choice(mimic_dict[kluch])
            print(kluch)

    return


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
