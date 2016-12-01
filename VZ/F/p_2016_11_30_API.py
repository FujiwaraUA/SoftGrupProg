# -*- coding: utf-8 -*-

import requests


class OpenweathermapAPI:
    """сайт http://openweathermap.org, дані по API"""
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
        except Exception as error:
            return "Exception (find_id):{}".format(error)

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
        except Exception as error:
            return "Exception (weather_forecast):{}".format(error)


city = 'Тернопіль'
find_id1 = OpenweathermapAPI()
find2 = find_id1.find_id(city)

if len(find2) == 2:
    city_id, city_owm = find2
else:
    city_owm = find2

# city_id, city_owm = find2 if len(find2) == 2 else city_owm = find2 - чому неправильно ?
print(city_owm)
forecast_Ternopil = find_id1.weather_forecast(city_id)
print(forecast_Ternopil[0])


