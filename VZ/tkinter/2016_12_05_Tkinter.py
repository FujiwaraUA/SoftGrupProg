# -*- coding: utf-8 -*-
import tkinter
import requests


class OpenweathermapAPI:
    """сайт http://openweathermap.org, дані по API."""

    def __init__(self):
        self.url_find = 'http://api.openweathermap.org/data/2.5/find'
        self.url_forecast = 'http://api.openweathermap.org/data/2.5/forecast'
        self.city_id = 0
        self.appid = '1bb8b7a186b957c05745fd9c421fd44c'

    def find_id(self, city):
        """Знайти ID міста по назві.(назва міста і країна з бази сайта). """
        try:
            self.city = city
            self.parameters = {'q': city,  # Місто
                               'APPID': self.appid}  # API ключ
            self.r = requests.get(self.url_find, params=self.parameters)
            self.data_json = self.r.json()
            self.city_id = self.data_json['list'][0]['id']  # ID міста
            self.city_country = '{} ({})'.format(self.data_json['list'][0]['name'],
                                                 self.data_json['list'][0]['sys']['country'])
            return self.city_id, self.city_country
        except Exception as e:
            return "Exception (find_id):{}".format(e)

    def weather_forecast(self, city_id):
        """Отримати погоду по id. """
        try:
            self.parameters = {'id': city_id,  # Місто
                               'units': 'metric',  # температури в одиницях градуси цельсія
                               'lang': 'uk',  # мова ( Ukrainian - uk (or ua))
                               'APPID': self.appid}  # API ключ
            self.r = requests.get(self.url_forecast, params=self.parameters)
            self.ls1 = []
            self.str_api = ''
            self.data_json = self.r.json()
            for i in self.data_json['list']:
                self.date = i['dt_txt'].split(' ')
                self.forecast = '{0} {1:+3.0f} {2}\n'.format(self.date[1][:5],
                                                             i['main']['temp'],
                                                             i['weather'][0]['description'])
                if self.date[0] in self.ls1:
                    self.str_api += self.forecast
                else:
                    self.ls1.append(self.date[0])
                    self.str_api += '\n{0:^14}\n\n'.format(self.date[0])
                    self.str_api += self.forecast
            return self.str_api, self.ls1
        except Exception as e:
            return "Exception (weather_forecast):{}".format(e)


def output(event):
    global id1
    s = ent1.get()
    s1 = api1.find_id(s)
    lab1_1['text'] = 'Місто: ' + s1[1]
    lab1_2['text'] = 'id: ' + str(s1[0])
    id1 = s1[0]

def output1(event):
    global id1
    s2 = api1.weather_forecast(id1)
    lab2['text'] = s2[0]

id1 = 0

root = tkinter.Tk()
root.title('Прогноз погоди')
root.geometry('500x850+300+100')

ent1 = tkinter.Entry(root)
but1 = tkinter.Button(root, text='Отримати id')
but2 = tkinter.Button(root, text='Погода')
fra1 = tkinter.Frame(root)
lab1_1 = tkinter.Label(fra1)
lab1_2 = tkinter.Label(fra1)
lab2 = tkinter.Label(root, justify='left')


ent1.grid(row=0, column=0, padx=20)
but1.grid(row=0, column=1, padx=20)
fra1.grid(row=1, column=0, padx=20)
but2.grid(row=1, column=1, padx=20)
lab2.grid(row=2, column=0, padx=20)

lab1_1.grid(row=0, column=0)
lab1_2.grid(row=1, column=0)

api1 = OpenweathermapAPI()


but1.bind("<Button-1>", output)
but2.bind("<Button-1>", output1)
root.mainloop()
