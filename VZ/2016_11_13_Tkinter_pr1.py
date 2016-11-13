# -*- coding: utf-8 -*-
import tkinter

i = 0


def naz(event):
    global i
    i += 1
    print(type(event))
    print('*' * 20)
    print(event)
    print('Кількість нажимань на кнопку "Друк": {}'.format(i))
    return i


root = tkinter.Tk()
but = tkinter.Button(root, text='Друк')

but.bind('<Button-1>', naz)
but.pack()
root.mainloop()
