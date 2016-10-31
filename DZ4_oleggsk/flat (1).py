""" Ремонт в квартирі 

Є квартира (2 кімнати і кухня). В квартирі планується ремонт:
потрібно наклеїти шпалери, пофарбувати стелі і вкласти підлоги.

Необхідно розрахувати вартість матеріалів для ремонту.

Із опису випливають наступні класи:
= Будівельні матеріали
  = Шпалери
  = Фарба для стелі
  = Ламінат
= Кімната
= Квартира

Детальніше, з методами (+) і атрибутами (-):
= Будівельні матеріали
  - площа (кв. м)
  - ціна за одиницю (рулон, банка, упаковка)
  = Шпалери
    - ширина рулону
    - довжина рулону
  = Фарба для стелі
    - вага банки
    - витрати фарби
  = Ламінат
    - дожина дошки
    - ширина дошки
    - кількість дошок в упаковці
= Кімната
  - ширина
  - висота
  - довжина
  - ширина вікна
  - ширина дверей
  + наклеїти шпалери
  + пофврбувати стелю
  + вкласти підлогу
  + підрахувати кошторис на кімнату
  + при створенні кімнати відразу передавати всі атрибути в конструктор __init__()
= Квартира
  - кімнати
  + добавити кімнату
  + видалити кімнату
  + підрахувати кошторис на всю квартиру
  + при створенні потрібно передати відразу всі кімнати в конструктор

Необхідно створити будматеріали, призначити їм ціни і розміри.
Створити кімнати, наклеїти, пофарбувати і вкласти все на свої місця.
Cтворити квартиру, присвоїти їй кімнати і підрахувати загальний кошторис.

Підсказка: для заокруглення вверх і вниз використовуйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Для простоти, будемо вважати, що шпалери над вікном і над дверима 
не наклеюються.
----------------

Додатково:
Зробіть в об’єкта квартири метод, який виводить результат в виді кошторису:

[Кімната: ширина: 3 м, довжина: 5 м, висота: 2.4 м]
Шпалери      400x6=2400 грн.
Фарба       1000x1=1000 грн.
Ламінат      800x8=6400 грн.
[Кімната: ширина: 3 м, довжина: 4 м, висота: 2.4 м]
Шпалери      400x5=2000 грн.
Фарба       1000x1=1000 грн.
Ламінат      800x7=5600 грн.
[Кухня: ширина: 3 м, довжина: 3 м, висота: 2.4 м]
Шпалери      400x4=1600 грн.
Фарба       1000x1=1000 грн.
Ламінат      800x5=4000 грн.
---------------------------
Всього: 25000 грн.

"""
import math


class Material(object):
    def __init__(self, price):
        self.price = price


class Wallpaper(Material):
    def __init__(self, price, length, width):
        super().__init__(price)
        self.length = length
        self.width = width

    def quantity(self, area):
        return math.ceil(area / (self.length * self.width))


class Paint(Material):
    def __init__(self, price, weight, usage):
        super().__init__(price)
        self.weight = weight
        self.usage = usage

    def quantity(self, area):
        return math.ceil(area / (self.weight / self.usage))


class Laminate(Material):
    def __init__(self, price, length, width, pcs):
        super().__init__(price)
        self.length = length
        self.width = width
        self.pcs = pcs

    def quantity(self, area):
        return math.ceil(area / (self.length * self.width * self.pcs))


class Room(object):
    def __init__(self, width, height, length, window_width, door_width):
        self.width = width
        self.height = height
        self.length = length
        self.window_width = window_width
        self.door_width = door_width
        self.wallpaper_qtt = 0
        self.paint_qtt = 0
        self.laminate_qtt = 0
        self.wallpaper_price = 0
        self.paint_price = 0
        self.laminate_price = 0

    def glue_wallpaper(self, wallpaper):
        self.wallpaper_price = wallpaper.price
        self.wallpaper_qtt = wallpaper.quantity(((self.width + self.length)*2 - self.window_width -
                                                 self.door_width) * self.height)

    def paint_ceiling(self, paint):
        self.paint_price = paint.price
        self.paint_qtt = paint.quantity(self.length * self.width)

    def mount_floor(self, laminate):
        self.laminate_price = laminate.price
        self.laminate_qtt = laminate.quantity(self.length * self.width)

    def get_cost(self):
        return self.wallpaper_qtt*self.wallpaper_price + self.paint_qtt*self.paint_price + \
               self.laminate_qtt*self.laminate_price


class Flat(object):
    def __init__(self, rooms):
        self.rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    def get_total_cost(self):
        total_cost = 0
        for room in self.rooms:
            total_cost += room.get_cost()
        return total_cost

    def get_estimate(self):
        total_cost = 0
        print('_________КОШТОРИС________')
        for room in self.rooms:
            total_cost += room.get_cost()
            print('[Кімната: ширина: {0} м, довжина: {1} м, висота: {2} м]'.format(room.width, room.length, room.height))
            print('Шпалери      {0}x{1}={2} грн.'.format(room.wallpaper_price, room.wallpaper_qtt,
                                                         room.wallpaper_price * room.wallpaper_qtt))
            print('Фарба        {0}x{1}={2} грн.'.format(room.paint_price, room.paint_qtt,
                                                         room.paint_price * room.paint_qtt))
            print('Ламінат      {0}x{1}={2} грн.'.format(room.laminate_price, room.laminate_qtt,
                                                         room.laminate_price * room.laminate_qtt))
        print('---------------------------\nВсього: {0} грн'.format(total_cost))


wallpaper = Wallpaper(235, 10, 1.2)
paint = Paint(327, 3, 0.25)
laminate = Laminate(187, 2, 0.35, 10)

kitchen = Room(3, 3.5, 4, 1.8, 1.2)
bedroom = Room(4.2, 3.5, 4.8, 2.2, 1.4)
living_room = Room(5.1, 3.5, 6, 2.5, 1.4)

kitchen.glue_wallpaper(wallpaper)
kitchen.paint_ceiling(paint)
kitchen.mount_floor(laminate)

bedroom.glue_wallpaper(wallpaper)
bedroom.paint_ceiling(paint)
bedroom.mount_floor(laminate)

living_room.glue_wallpaper(wallpaper)
living_room.paint_ceiling(paint)
living_room.mount_floor(laminate)

my_flat = Flat([kitchen, bedroom, living_room])

print('Ціна матеріалів на кухню %s' % kitchen.get_cost())
print('Ціна матеріалів на спальню %s' % bedroom.get_cost())
print('Ціна матеріалів на вітальню %s' % living_room.get_cost())
print('Ціна матеріалів на всю квартиру %s' % my_flat.get_total_cost())
print(my_flat.get_estimate())
