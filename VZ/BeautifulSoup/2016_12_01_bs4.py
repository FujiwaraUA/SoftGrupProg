# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

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
            str_parse += '\n{0:^14}\n\n'.format(ls_days[i])
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
parse(html_text)

