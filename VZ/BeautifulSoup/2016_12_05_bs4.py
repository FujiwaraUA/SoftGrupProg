# -*- coding: utf-8 -*-
import requests
import tkinter
from bs4 import BeautifulSoup


def window(str_parse):
    root = tkinter.Tk()
    root.title('Прогноз погоди')
    root.geometry('500x850+300+100')

    # lab = tkinter.Label(root, text='API: openweathermap.org')
    # lab.grid(row=0, column=0, padx=20)
    #
    # lab_d1 = tkinter.Label(root, text=str_api, justify='left')
    # lab_d1.grid(row=1, column=0, padx=20)

    lab1 = tkinter.Label(root, text='Парсинг: Яндекс Погода')
    lab1.grid(row=0, column=2, padx=2)

    lab1_j1 = tkinter.Label(root, text=str_parse, justify='left')
    lab1_j1.grid(row=1, column=2, padx=2)
    root.mainloop()


class YandexWeatherParse:
    """сайт https://yandex.ua/pogoda/ternopol, Парсинг."""

    def __init__(self):
        self.url = 'https://yandex.ua/pogoda/ternopol/details'
        self.str_parse = ''
        self.ls_days = []

    def get_html(self):
        """Отримати HTML сторінку. """
        try:
            response = requests.get(self.url)
            return response.text
        except Exception as e:
            return "Exception (get_html):{}".format(e)

    def parse(self, html):
        """Отримати погоду з HTML сторінки. """
        try:
            self.soup = BeautifulSoup(html, 'html.parser')
            self.head = self.soup.find('h1', 'title title_level_1')
            self.str_parse += '{}\n'.format(self.head.text)
            self.days = self.soup.find_all('dt', 'forecast-detailed__day')
            for i in self.days:
                if 'data-anchor' in i.attrs:
                    self.day = i.attrs['data-anchor']
                    month_teg = i.find('span', 'forecast-detailed__day-month')
                    month = month_teg.text
                    self.ls_days.append('{0} {1}'.format(self.day, month))
            tables_weather = self.soup.find_all('table', 'weather-table')
            for i, value in enumerate(tables_weather):
                self.str_parse += '{0:^20}\n'.format(self.ls_days[i])
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
                    self.str_parse += '{}\n'.format(day_part_str)
            return self.str_parse
        except Exception as e:
            return "Exception (parse):{}".format(e)

pars1 = YandexWeatherParse()
html_text = pars1.get_html()
str_parse = pars1.parse(html_text)
window(str_parse)
