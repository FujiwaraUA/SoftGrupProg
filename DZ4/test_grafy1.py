# -*- coding: utf-8 -*-
import turtle
import time
import random

class Krug:
    def __init__(self, kolor):
        self.kolor = kolor
        self.t1 = turtle.Turtle()
        self.t1.hideturtle()

    def risuvati_kolo(self, x):
        self.x = x
        self.t1.color(self.kolor)  # встановлюємо колір лінії
        self.t1.penup()  # забираємо "ручку" від полотна, щоб перемістити в потрібне місце
        self.t1.setpos(self.x, 100)  # переміщаємо в "основу" - це буде сама низька точка
        self.t1.pendown()  # опускаєм ручку назад
        self.t1.circle(25)  # рисуємо коло радіусу 25




def main():
    turtle.tracer(0, 0)  # встановлюємо всі затримки в 0, щоб рисувалося миттєво
    turtle.hideturtle()  # забираємо точку на середині

    ttl = turtle.Turtle()  # створюємо об’єкт черепашки для рисування
    ttl.hideturtle()  # робимо її невидимою

    tt2 = Krug('violet')
    while True:
        time.sleep(1.5)  # засипаємо на пів секунди, щоб побачити що нарисували
        ttl.clear()  # очищаєм все нарисоване раніше
        tt2.t1.clear()
        x = random.randint(-200, 200)  # отримуємо випадкові координати
        tt2.risuvati_kolo(x)
        turtle.update()  # так як зробили turtle.tracer(0, 0) потрібно оновити екран, щоб побачити нарисоване


if __name__ == '__main__':
    main()