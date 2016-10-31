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
import time
import random

FIELDSIZE_X = 800
FIELDSIZE_Y = 600


class Polygon(turtle.Turtle):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        self.color(color)
        self.hideturtle()
        self.clear()
        self.vector = 0

    def mov_to(self, x, y):
        self.x = x
        self.y = y
        self.draw()

    def erase(self):
        self.clear()

    def mov_up(self, step):
        self.y += step
        self.draw()

    def mov_dn(self, step):
        self.y -= step
        self.draw()

    def mov_lft(self, step):
        self.x -= step
        self.draw()

    def mov_rt(self, step):
        self.x += step
        self.draw()

    def mov_vector(self, step, angle=None):  # Move polygon in certain vector for certain step (angle 0 - North)
        if angle is not None:
            self.vector = angle
        self.penup()
        self.setpos(self.x, self.y)
        self.setheading(90 - self.vector)
        self.forward(step)
        self.x, self.y = self.position()
        self.draw()

    def size(self, size):
        self.size = size
        self.draw()

    def set_angle(self, angle):
        self.angle = angle
        self.draw()

    def rotate_cw(self, angle):
        self.angle += angle
        self.draw()

    def rotate_ccw(self, angle):
        self.angle -= angle
        self.draw()

    def reset_angle(self):
        self.angle = 0
        self.draw()

    def set_color(self, color):
        self.color(color)
        self.draw()

    def out_of_field(self, fieldsize_x, fieldsize_y):
        if abs(self.x - self.size) > fieldsize_x/2 or abs(self.y - self.size) > fieldsize_y:
            return True
        else:
            return False

    def on_bottom(self, fieldsize_Y):
        if (self.y - self.size/2) <= -fieldsize_Y/2:
            return True
        else:
            return False


class Square(Polygon):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def draw(self):
        self.clear()
        self.penup()
        self.setheading(0 - self.angle)
        self.setpos(self.x, self.y)
        self.forward(self.size/2)
        self.right(90)
        self.pendown()
        self.forward(self.size/2)
        self.right(90)
        self.forward(self.size)
        self.right(90)
        self.forward(self.size)
        self.right(90)
        self.forward(self.size)
        self.right(90)
        self.forward(self.size/2)


class Triangle(Polygon):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def draw(self):
        self.clear()
        self.penup()
        self.setheading(270 - self.angle)
        self.setpos(self.x, self.y)
        self.forward((self.size*1.732050807568877)/6)
        self.right(90)
        self.pendown()
        self.forward(self.size/2)
        self.right(120)
        self.forward(self.size)
        self.right(120)
        self.forward(self.size)
        self.right(120)
        self.forward(self.size/2)


class Circle(turtle.Turtle):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        self.color(color)
        self.hideturtle()
        self.clear()
        self.vector = 0

    def draw(self):
        self.clear()
        self.penup()
        self.setheading(0)
        self.setpos(self.x, self.y - self.size)
        self.pendown()
        self.circle(self.size)

    def erase(self):
        self.clear()

    def set_angle(self, angle):
        self.angle = angle
        self.draw()

    def mov_to(self, x, y):
        self.x = x
        self.y = y
        self.draw()

    def mov_up(self, step):
        self.y += step
        self.draw()

    def mov_dn(self, step):
        self.y -= step
        self.draw()

    def mov_lft(self, step):
        self.x -= step
        self.draw()

    def mov_rt(self, step):
        self.x += step
        self.draw()

    def mov_vector(self, step, angle=None):  # Move polygon in certain vector for certain step (angle 0 - North)
        if angle is not None:
            self.vector = angle
        self.penup()
        self.setpos(self.x, self.y)
        self.setheading(90 - self.vector)
        self.forward(step)
        self.x, self.y = self.position()
        self.draw()

    def size(self, size):
        self.size = size
        self.draw()

    def set_color(self, color):
        self.color(color)
        self.draw()

    def out_of_field(self, fieldsize_x, fieldsize_y):
        if abs(self.x - self.size) > fieldsize_x/2 or abs(self.y - self.size) > fieldsize_y:
            return True
        else:
            return False

    def on_bottom(self, fieldsize_Y):
        if (self.y - self.size) <= -fieldsize_Y/2:
            return True
        else:
            return False

######################################################################################################


def get_random_figure():
    return random.choice([Triangle, Square, Circle])


def get_random_color():
    return random.choice(['black', 'red', 'blue', 'green', 'purple', 'yellow', 'orange'])


def get_random_size():
    return random.randint(20, 60)


def get_random_angle():
    return random.randint(0, 360)


def get_random_vector():
    return random.randint(120, 240)


def get_random_position():
    return random.randint(-FIELDSIZE_X/2, FIELDSIZE_X/2)


def chance():
    if random.randint(0, 10) == 4:
        return True
    else:
        return False

def spawn_new_object():
    color = get_random_color()
    size = get_random_size()
    x = get_random_position()
    y = FIELDSIZE_Y/2
    figure = get_random_figure()(x, y, size, color)
    figure.set_angle(get_random_angle())
    figure.vector = 180
    return figure


def main():

    turtle.tracer(0, 0)  # встановлюємо всі затримки в 0, щоб рисувалося миттєво
    turtle.hideturtle()  # забираємо точку на середині
    turtle.setup(height=FIELDSIZE_Y, width=FIELDSIZE_X)
    square = Square(0, 0, 60, 'blue')
    triangle = Triangle(0, 0, 50, 'red')
    circle = Circle(0, 0, 30, 'green')
    circle.draw()
    object_set = []

    while True:
        time.sleep(0.15)  # засипаємо на пів секунди, щоб побачити що нарисували
        square.rotate_cw(10)
        triangle.rotate_ccw(7)

        if chance():  # add new objects if needed
            object_set.append(spawn_new_object())

        if len(object_set) > 30:  # Limit figure count
            object_set[0].erase()
            object_set.pop(0)

        for obj in object_set:
            if not obj.on_bottom(FIELDSIZE_Y):
                if chance():
                    obj.mov_vector(5, angle=get_random_vector())
                else:
                    obj.mov_vector(5)
                if chance():
                    obj.set_color(get_random_color())

        turtle.update()  # так як зробили turtle.tracer(0, 0) потрібно оновити екран, щоб побачити нарисоване

if __name__ == '__main__':
    main()
