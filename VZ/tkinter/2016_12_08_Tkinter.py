# -*- coding: utf-8 -*-

import tkinter


class Window:
    """GUI"""

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Прогноз погоди')
        self.root.geometry('1000x750+300+150')
        self.title_label = tkinter.Label(self.root, text='ПОГОДНІ СЕРВІСИ', font='arial 20')
        self.api_button = tkinter.Button(self.root, width=25, text='API: openweathermap.org', font='arial 14')
        self.pars_button = tkinter.Button(self.root, width=25, text='Парсинг: Яндекс Погода', font='arial 14')
        self.root_frame = tkinter.Frame(self.root, width=950, height=500, bg='#CFD8DC', bd=10)

        self.title_label.grid(row=0, column=1, pady=5)
        self.api_button.grid(row=1, column=0, pady=20, padx=15)
        self.pars_button.grid(row=1, column=2, pady=20, padx=15)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)

        self.api_button.bind("<Button-1>", self.api_frame)
        self.pars_button.bind("<Button-1>", self.pars_frame)
        self.root.mainloop()

    def pars_frame(self, event):
        self.root_frame.grid_forget()
        self.root_frame = tkinter.Frame(self.root, width=950, height=500, bg='#CFD8DC', bd=10)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)


    def api_frame(self, event):
        self.root_frame.grid_forget()
        self.root_frame = tkinter.Frame(self.root, width=950, height=500, bg='#CFD8DC', bd=10)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)
        self.name_city_label = tkinter.Label(self.root_frame, text='Назва міста', font='arial 12', bg='#CFD8DC')
        self.name_city_entry = tkinter.Entry(self.root_frame, font='arial 14', bd=3)
        self.id_button = tkinter.Button(self.root_frame, width=25, text='Отримати ID міста.', font='arial 12')
        self.id_frame = tkinter.Frame(self.root_frame)
        self.city_label = tkinter.Label(self.id_frame, text='Місто:{}'.format('отримане місто'), font='arial 12', bg='#CFD8DC')
        self.id_label = tkinter.Label(self.id_frame, text='id:{}'.format('отримене ID'), font='arial 12', bg='#CFD8DC')
        self.weather_button = tkinter.Button(self.root_frame, width=25, text='Прогноз погоди / оновити.',
                                             font='arial 12')
        self.weather_frame = tkinter.Frame(self.root_frame, bg='#ECEFF1')
        self.day_1_label = tkinter.Label(self.weather_frame, text='day_1', font='arial 12', bg='#CFD8DC')
        self.day_2_label = tkinter.Label(self.weather_frame, text='day_2', font='arial 12', bg='#CFD8DC')
        self.day_3_label = tkinter.Label(self.weather_frame, text='day_3', font='arial 12', bg='#CFD8DC')
        self.day_4_label = tkinter.Label(self.weather_frame, text='day_4', font='arial 12', bg='#CFD8DC')
        self.day_5_label = tkinter.Label(self.weather_frame, text='day_5', font='arial 12', bg='#CFD8DC')
        self.day_6_label = tkinter.Label(self.weather_frame, text='day_6', font='arial 12', bg='#CFD8DC')
        self.name_city_label.grid(row=0, column=0, pady=20, padx=15)
        self.name_city_entry.grid(row=0, column=1, pady=20, padx=15)
        self.id_button.grid(row=0, column=2, pady=20, padx=15)
        self.id_frame.grid(row=1, column=1)
        self.city_label.pack(side='left')
        self.id_label.pack()
        self.weather_button.grid(row=1, column=2)
        self.weather_frame.grid(row=2, column=0, columnspan=3, pady=15, padx=25)
        self.day_1_label.grid(row=0, column=0, pady=5, padx=5)
        self.day_2_label.grid(row=0, column=1, pady=5, padx=5)
        self.day_3_label.grid(row=0, column=2, pady=5, padx=5)
        self.day_4_label.grid(row=1, column=0, pady=5, padx=5)
        self.day_5_label.grid(row=1, column=1, pady=5, padx=5)
        self.day_6_label.grid(row=1, column=2, pady=5, padx=5)


window_root = Window()
