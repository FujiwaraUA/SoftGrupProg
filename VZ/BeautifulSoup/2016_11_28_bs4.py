# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ua/pogoda/ternopol/details' # ?from=serp_title&ncrnd=9522'
#url = 'https://yandex.ua/pogoda/berezhani/details'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    dict1 = dict()
    soup = BeautifulSoup(html, 'html.parser')
    head = soup.find('div', 'navigation-city navigation-city_meteum i-bem')
    head = head.h1.text
    print(head)
    dict1[head.strip()] = []
    # print(dict1)
    table = soup.find('div', 'tabs-panes__pane tabs-panes__pane_active_yes')
    jac_data = table.find_all('dt', 'forecast-detailed__day')
    # print(len(jac_data))
    # print(type(jac_data[0]))
    # print(jac_data[0].prettify())
    # print(jac_data[0].small.text)
    # print(jac_data[0].attrs)
    # print(jac_data[0]['data-anchor'])
    # print(jac_data[0].strong.span.text)
    ls1 = []
    for i in range(len(jac_data)):
        if 'data-anchor' in jac_data[i].attrs:
            # print(jac_data[i]['data-anchor'], end=' ')
            #print(jac_data[i].prettify())
            mis = jac_data[i].find('span', 'forecast-detailed__day-month')
            # print(mis.text)
            a = jac_data[i]['data-anchor'] + ' ' + mis.text
            ls1.append(a)
    # print(ls1)

    jac_data1 = table.find_all('dd', 'forecast-detailed__day-info')
    ls2 = []
    n = -1

    for i in range(len(jac_data1)):
        if len(jac_data1[i].attrs['class']) < 2:
            # print(i)
            ls2.append([])
            table1 = jac_data1[i].find('tbody')
            table2 = table1.find_all('td', 'weather-table__body-cell weather-table__body-cell_type_daypart')
            n += 1
            print('')
            print(ls1[n])
            print('')
            for i in range(len(table2)):
                table3 = table2[i].find_all('div')
                print('{0:7} {1}'.format(table3[0].text, table3[1].text))

        elif jac_data1[i].attrs['class'][1] != 'ad':
            # print(i)
            table1 = jac_data1[i].find('tbody')
            table2 = table1.find_all('td', 'weather-table__body-cell weather-table__body-cell_type_daypart')
            n += 1
            print('')
            print(ls1[n])
            print('')
            for i in range(len(table2)):
                table3 = table2[i].find_all('div')
                print('{0:7} {1}'.format(table3[0].text, table3[1].text))








def main():
    parse(get_html(url))


if __name__ == '__main__':
    main()
