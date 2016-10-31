"""
Це приклад невеликої програми для малювання кругів і квадратів.
Вам потрібно на основі цієї програми зробити невелику "танцювальну" сценку з
використанням кругів, квардратів і трикутників. Зробити все це потрібно в
об’єктно-орієнтованому стилі.

Які класи потрібно реалізувати:

- Багатокутник (на його основі зробити квадрат і правильний трикутник)
-- клас повинен вміти відрисовувати себе
-- переміщатися в деякому напряику заданому координатами x, y
-- збільшуватися (необов’язково)
-- повертатися (необов’язково)

- Квардрат (успадковується від багаткутника)
-- метод __init__ приймає координати середини, ширину і колір

- Трикутник (успадковується від багатокутника)
-- метод __init__ приймає координати середини, довжини сторони і колір

- Коло
-- метод __init__ приймає координати середини, радіус і колір
-- клас повинен вміти відрисовувати себе
-- преміщатися в деякому напрямку заданому координатами x, y
-- збільшуватися (необов’язково)

Також рекомендую створити додатковий клас Vector для представлення
точок на площині і різних операцій з ними - додавання, множення на число,
віднімання.


Із створених класів потрібно скласти якусь динамічну сцену.
"""

import turtle
from time import sleep
from random import randint

class polygon_drawer:
    """docstring for polygon_drawer"""
    
    def move(self, x, y):
        self.ttl.setpos(x, y) # переміщаємо на першу вершину

    def draw(self, angles, size):
        self.ttl.pendown()
        for i in range(angles):
            self.ttl.forward(size)
            self.ttl.right(360 / angles)
        self.ttl.penup()

    def __init__(self):
        super(polygon_drawer, self).__init__()
        self.ttl = turtle.Turtle()
        self.ttl.hideturtle()
        self.ttl.penup()
        turtle.tracer(0, 0)
        
class square(polygon_drawer):
    """docstring for square"""
    def draw(self, size):
        self.ttl.pendown()
        for i in range(4):
            self.ttl.forward(size)
            self.ttl.right(90)
        self.ttl.penup()

    def __init__(self, x, y, size, color):
        super(square, self).__init__()
        self.ttl.color = color
        self.move(x, y)
        self.draw(size)


class triangle(polygon_drawer):
    """docstring for square"""
    def draw(self, size):
        self.ttl.pendown()
        for i in range(3):
            self.ttl.forward(size)
            self.ttl.left(120)
        self.ttl.penup()

    def __init__(self, x, y, size, color):
        super(triangle, self).__init__()
        self.ttl.color(color)
        self.move(x, y)
        self.draw(size)

class circle(polygon_drawer):
    """docstring for square"""
    def draw(self, size):
        self.ttl.pendown()
        self.ttl.circle(size)
        self.ttl.penup()

    def __init__(self, x, y, size, color):
        super(circle, self).__init__()
        self.ttl.color(color)
        self.move(x, y)
        self.draw(size)

def main():
    colors = ['red', 'green', 'blue', 'yellow', 'violet', 'black']
    while True:
        a = circle(randint(-200, 200), randint(-200, 200), randint(5, 50), colors[randint(0, 5)])
        b = square(randint(-200, 200), randint(-200, 200), randint(5, 50), colors[randint(0, 5)])
        c = triangle(randint(-200, 200), randint(-200, 200), randint(5, 50), colors[randint(0, 5)])
        turtle.update() # так як зробили turtle.tracer(0, 0) потрібно оновити екран, щоб побачити нарисоване
        sleep(0.5) # засипаємо на пів секунди, щоб побачити що нарисували
        a.ttl.clear()
        b.ttl.clear()
        c.ttl.clear()

if __name__ == '__main__':
    main()
