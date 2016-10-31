import turtle
import time
import random


def draw_circle(ttl):
    x = random.randint(-200, 200)  # отримуємо випадкові координати
    y = random.randint(-200, 200)

    ttl.color('violet')  # встановлюємо колір лінії
    ttl.penup()  # забираємо "ручку" від полотна, щоб перемістити в потрібне місце
    ttl.setpos(x, y)  # переміщаємо в "основу" - це буде сама низька точка
    ttl.pendown()  # опускаєм ручку назад

    ttl.circle(25)  # рисуємо коло радіусу 25


def main():
    turtle.tracer(0, 0)  # встановлюємо всі затримки в 0, щоб рисувалося миттєво
    turtle.hideturtle()  # забираємо точку на середині

    ttl = turtle.Turtle()  # створюємо об’єкт черепашки для рисування
    ttl.hideturtle()  # робимо її невидимою

    while True:
        time.sleep(0.5)  # засипаємо на пів секунди, щоб побачити що нарисували
        ttl.clear()  # очищаєм все нарисоване раніше
        draw_circle(ttl)
        turtle.update()  # так як зробили turtle.tracer(0, 0) потрібно оновити екран, щоб побачити нарисоване


if __name__ == '__main__':
    main()
