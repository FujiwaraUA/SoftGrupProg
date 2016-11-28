# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ua/pogoda/ternopol/details?from=serp_title&ncrnd=9522'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    head = soup.find('div', 'navigation-city navigation-city_meteum i-bem')
    head = head.h1.text
    print(head)
    table = soup.find('div', 'tabs-panes__pane tabs-panes__pane_active_yes')
    jac_data = table.find_all('dt', 'forecast-detailed__day')
    # print(len(jac_data))
    # print(type(jac_data[0]))
    # print(jac_data[0].prettify())
    # print(jac_data[0].small.text)
    # print(jac_data[0].attrs)
    # print(jac_data[0]['data-anchor'])
    # print(jac_data[0].strong.span.text)
    for i in range(len(jac_data)):
        if 'data-anchor' in jac_data[i].attrs:
            print(jac_data[i]['data-anchor'], end=' ')
            #print(jac_data[i].prettify())
            mis = jac_data[i].find('span', 'forecast-detailed__day-month')
            print(mis.text)






def main():
    parse(get_html(url))


if __name__ == '__main__':
    main()
