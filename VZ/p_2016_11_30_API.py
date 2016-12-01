# -*- coding: utf-8 -*-

import requests
import tkinter
from bs4 import BeautifulSoup

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


def window(str_api, str_parse):
    root = tkinter.Tk()
    root.title('Прогноз погоди')
    root.geometry('500x800+300+100')
    lab = tkinter.Label(root, text='API: openweathermap.org')
    lab.grid(row=0, column=0, padx=20)

    lab_d1 = tkinter.Label(root, text=str_api, justify='left')
    lab_d1.grid(row=1, column=0, padx=20)

    lab1 = tkinter.Label(root, text='Парсинг: Яндекс Погода')
    lab1.grid(row=0, column=2, padx=2)

    lab1_j1 = tkinter.Label(root, text=str_parse, justify='left')
    lab1_j1.grid(row=1, column=2, padx=2)
    root.mainloop()


'''Поки функцією'''

url = 'https://yandex.ua/pogoda/ternopol/details'

def get_html(url):
    """Отримати HTML сторінку. """
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return "Exception (get_html):{}".format(e)

def parse(html):
    """Отримати погоду з HTML сторінки. """
    try:
        str_parse = ''
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.find('h1', 'title title_level_1')
        str_parse += '{}\n'.format(head.text)
        days = soup.find_all('dt', 'forecast-detailed__day')
        ls_days = []
        for i in days:
            if 'data-anchor' in i.attrs:
                day = i.attrs['data-anchor']
                month_teg = i.find('span', 'forecast-detailed__day-month')
                month = month_teg.text
                ls_days.append('{0} {1}'.format(day, month))
        tables_weather = soup.find_all('table', 'weather-table')
        for i, value in enumerate(tables_weather):
            str_parse += '{0:^20}\n'.format(ls_days[i])
            row = value.find_all('tr', 'weather-table__row')
            for day_part in row:
                day_part_name = day_part.find('div', 'weather-table__daypart')
                day_part_name = day_part_name.text
                day_part_t = day_part.find('div', 'weather-table__temp')
                day_part_t = day_part_t.text
                day_part_v_td = day_part.find('td', 'weather-table__body-cell_type_condition')
                day_part_v = day_part_v_td.find('div', 'weather-table__value')
                day_part_v = day_part_v.text
                day_part_str = '{0:7} {1:7} {2}'.format(day_part_name, day_part_t, day_part_v)
                str_parse += '{}\n'.format(day_part_str)
        return str_parse
    except Exception as e:
        return "Exception (parse):{}".format(e)


html_text = get_html(url)
str_parse = parse(html_text)




'''
на період відладки

city = 'Тернопіль'
find_id1 = OpenweathermapAPI()
find2 = find_id1.find_id(city)

if len(find2) == 2:
    city_id, city_owm = find2
else:
    city_owm = find2
'''
city_id, city_owm = (691650, 'Ternopil (Ukraine)')
find_id1 = OpenweathermapAPI()

# city_id, city_owm = find2 if len(find2) == 2 else city_owm = find2 - чому неправильно ?
forecast_Ternopil = find_id1.weather_forecast(city_id)

str_api = '{0}\n{1}'.format(city_owm, forecast_Ternopil[0])
# str_parse = 'parse'

window(str_api, str_parse)
