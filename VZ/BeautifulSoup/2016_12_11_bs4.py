# -*- coding: utf-8 -*-

import requests
import tkinter
from bs4 import BeautifulSoup


class YandexWeatherParse:
    """сайт https://yandex.ua/pogoda/ternopol, Парсинг."""

    def __init__(self):
        self.url = 'https://yandex.ua/pogoda/ternopol/details'
        self.str_parse = ''
        self.ls_days = []
        self.ls_days2 = []

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
                self.ls_days2.insert(i, '{0:^20}\n'.format(self.ls_days[i]))
                row = value.find_all('tr', 'weather-table__row')
                for day_part in row:
                    day_part_name = day_part.find('div', 'weather-table__daypart')
                    day_part_name = day_part_name.text
                    day_part_t = day_part.find('div', 'weather-table__temp')
                    day_part_t = day_part_t.text
                    day_part_v_td = day_part.find('td', 'weather-table__body-cell_type_condition')
                    day_part_v = day_part_v_td.find('div', 'weather-table__value')
                    day_part_v = day_part_v.text
                    if len(day_part_t) < 3:
                        day_part_str = '{0:7} {1:8} {2}'.format(day_part_name, day_part_t, day_part_v)
                    else:
                        day_part_str = '{0:7} {1:7} {2}'.format(day_part_name, day_part_t, day_part_v)
                    self.str_parse += '{}\n'.format(day_part_str)
                    self.ls_days2[i] += '{}\n'.format(day_part_str)
            return self.head.text, self.ls_days2
        except Exception as e:
            return "Exception (parse):{}".format(e)


pars = YandexWeatherParse()
htmlt = pars.get_html()
print(pars.parse(htmlt)[0])
print(pars.parse(htmlt)[1][0])
