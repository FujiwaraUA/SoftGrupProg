# -*- coding: utf-8 -*-
import tkinter
ls1 = ['2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04']
dict1 = {'2016-12-01': {'Вночі': '-1   +1', 'Вранці': '+1   +1', 'Увечері': '+1   +1', 'Вдень': '+0   +1'},
         '2016-12-03': {'Вночі': '-3   -2', 'Вранці': '-3   -2', 'Увечері': '-2   -1', 'Вдень': '-2   -1'},
         '2016-12-04': {'Вночі': '-3   -0', 'Вранці': '-0   +1', 'Увечері': '+0   +1', 'Вдень': '+1   +1'},
         '2016-12-02': {'Вночі': '+0   +1', 'Вранці': '-1   +0', 'Увечері': '-1   -0', 'Вдень': '-2   -1'}}


root = tkinter.Tk()
root.title('Форма з погодою')
root.geometry('500x400+300+200')
lab = tkinter.Label(root, text='API: openweathermap.org')
lab.grid(row=0, column=0, padx=20)

lab_d1 = tkinter.Label(root, text=ls1[0])
lab_d1.grid(row=1, column=0, padx=20)

lab_d2 = tkinter.Label(root, text='Вранці {}'.format(dict1[ls1[0]]['Вранці']))
lab_d2.grid(row=2, column=0, padx=20)

lab_d3 = tkinter.Label(root, text='Вдень {}'.format(dict1[ls1[0]]['Вдень']))
lab_d3.grid(row=3, column=0, padx=20)

lab1 = tkinter.Label(root, text='Парсінг: Яндекс Погода')
lab1.grid(row=0, column=2, padx=2)

root.mainloop()
