# -*- coding: utf-8 -*-
import tkinter
from p_2016_11_22_API_1 import str_api
from p_2016_11_28_bs4 import stroka
print('API словарь')
print(str_api)
#
print('Парсінг Погода яндекс')
print(stroka)

root = tkinter.Tk()
root.title('Погодний аналізатор')
root.geometry('500x800+300+100')
lab = tkinter.Label(root, text='API: openweathermap.org')
lab.grid(row=0, column=0, padx=20)

lab_d1 = tkinter.Label(root, text=str_api)
lab_d1.grid(row=1, column=0, padx=20)


lab1 = tkinter.Label(root, text='Парсінг: Яндекс Погода')
lab1.grid(row=0, column=2, padx=2)

lab1_j1 = tkinter.Label(root, text=stroka)
lab1_j1.grid(row=1, column=2, padx=2)
root.mainloop()
