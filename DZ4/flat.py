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

class BuildMater:
    """Будівельні матеріали"""
    def __init__(self, price_per_unit):
        self.square = 0
        self.price_per_unit = price_per_unit


class Wallpaper(BuildMater):
    """Шпалери"""
    def __init__(self, roll_width, roll_length, price_per_unit):
        BuildMater.__init__(self, price_per_unit)
        self.roll_width = roll_width
        self.roll_length = roll_length
        self.square = self.roll_width * self.roll_length



class Paint(BuildMater):
    """Фарба"""
    def __init__(self, weight, weight_square, price_per_unit ):
        BuildMater.__init__(self, price_per_unit )
        self.weight = weight
        self.weight_square = weight_square
        self.square = self.weight / self.weight_square


class Laminate(BuildMater):
    """Ламінат"""
    def __init__(self, board_width, board_length, board_count_in_pack, price_per_unit):
        BuildMater.__init__(self, price_per_unit)
        self.board_width = board_width
        self.board_length = board_length
        self.board_count_in_pack = board_count_in_pack
        self.square = self.board_width * self.board_length * self.board_count_in_pack


class Room:
    """Кімната"""
    def __init__(self, width, height, length, w, b, d, width_window=0, width_door=0):
        self.width = width
        self.height = height
        self.length = length
        self.width_window = width_window
        self.width_door = width_door
        self.w = w
        self.b = b
        self.d = d
    def glueWallpapers(self):
        square = ((self.width * self.height * 2) + (self.length * self.height * 2))\
                 - (self.width_door * self.height) - (self.width_door * self.height)
        rulon = math.ceil(square / self.w.square)
        soum = rulon * self.w.price_per_unit
        return 'Шпалери      {:>4}x{:<2}={:>5} грн.'.format(self.w.price_per_unit, rulon, soum)


    def paintCeiling(self):
        square = self.width * self.length
        jar = math.ceil(square * self.b.weight_square / self.b.weight)
        soum = jar * self.b.price_per_unit
        return 'Фарба        {:>4}x{:<2}={:>5} грн.'.format(self.b.price_per_unit, jar, soum)


    def putFloor(self):
        square = self.width * self.length
        pack = math.ceil(square / self.d.square)
        soum = pack * self.d.price_per_unit
        return 'Ламінат      {:>4}x{:<2}={:>5} грн.'.format(self.d.price_per_unit, pack, soum)


    def calculate(self):
        print(self.glueWallpapers())
        print(self.paintCeiling())
        print(self.putFloor())



class Flat:
    """Квартира"""
    def __init__(self, rooms):
        self.rooms = rooms

    def addRoom(self,name_room, room):
        self.rooms[name_room] = room

    def delRoom(self, name):
        del self.rooms[name]

    def calculate(self):
        for key in self.rooms:
            print('{0:10}: ширина: {1} м, довжина: {2} м, висота: {3} м'.format(key, self.rooms[key].width,
                                                                         self.rooms[key].length,
                                                                         self.rooms[key].height))
            self.rooms[key].calculate()



w1 = Wallpaper(0.5, 10, 65)
b1 = Paint(7, 0.5, 200)
d1 = Laminate(0.14,2,20,500)


rooms = {}
rooms['Кімната1'] = (Room(3, 2.4, 5, w1,b1,d1))
rooms['Кімната2'] = (Room(3, 2.4, 4,w1,b1,d1))
rooms['Кухня'] = (Room(3, 2.4, 3, w1, b1,d1))

r = Flat(rooms)

r.addRoom('wana', Room( 3, 2.4, 5, w1,b1,d1))
r.delRoom('wana')
r.calculate()




