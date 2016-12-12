# -*- coding: utf-8 -*-
import tkinter
import requests
from bs4 import BeautifulSoup


class Window:
    """GUI"""

    def __init__(self, owmapi, pars):
        self.id = 0
        self.owmapi = owmapi
        self.pars = pars
        self.id_name = ()
        self.root = tkinter.Tk()
        self.root.title('Прогноз погоди')
        self.root.geometry('1200x800+200+100')
        self.title_label = tkinter.Label(self.root, text='ПОГОДНІ СЕРВІСИ', font='arial 20')
        self.api_button = tkinter.Button(self.root, width=25, text='API: openweathermap.org', font='arial 14')
        self.pars_button = tkinter.Button(self.root, width=25, text='Парсинг: Яндекс Погода', font='arial 14')
        self.root_frame = tkinter.Frame(self.root, width=1150, height=500, bg='#CFD8DC', bd=10)

        self.title_label.grid(row=0, column=1, pady=5)
        self.api_button.grid(row=1, column=0, pady=20, padx=15)
        self.pars_button.grid(row=1, column=2, pady=20, padx=15)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)

        self.api_button.bind('<Button-1>', self.api_frame)
        self.pars_button.bind('<Button-1>', self.pars_frame)
        self.root.mainloop()

    def pars_frame(self, event):
        self.ls_city = ['Іване-Пусте', 'Бережани', 'Борщів', 'Борщівка', 'Бучач', 'Білозірка', 'Великий Глибочок',
                        'Великі Бірки', 'Вишгородок', 'Вишнівець', 'Горинка', 'Гримайлів', 'Гусятин', 'Дарахів',
                        'Джурин', 'Доброполе', 'Дружба', 'Дунаїв', 'Завалів', 'Заводське', 'Залізці', 'Заліщики',
                        'Збараж', 'Зборів', 'Золотий Потік', 'Золотники', 'Ковалівка', 'Козлів', 'Козова', 'Колодне',
                        'Копичинці', 'Коропець', 'Кременець', 'Куряни', 'Ланівці', 'Літятин', 'Максимівка',
                        'Мельниця-Подільська', 'Микулинці', 'Млинівці, Зборівський район',
                        'Млинівці, Кременецький район', 'Монастириська', 'Плотича', 'Почаїв', 'Пробіжна',
                        'Підволочиськ', 'Підгайці', 'Скала-Подільська', 'Скалат', 'Теребовля', 'Тернопіль',
                        'Товсте, Гусятинський район', 'Товсте, Заліщицький район', 'Токи', 'Устя-Зелене',
                        'Хоростків', 'Чернихівці', 'Чортків', 'Шумляни', 'Шумськ', 'Яблунів']
        self.dict_city = {'Тернопіль': 'ternopol', 'Чернихівці': 'chernihovtsy', 'Золотий Потік': 'zolotoy-potok',
                          'Борщів': 'borshchev', 'Гримайлів': 'grimaylov', 'Млинівці, Зборівський район': 'mlinovci',
                          'Заліщики': 'zalishchiki', 'Великі Бірки': 'velikie-borki', 'Плотича': 'plotycha',
                          'Чортків': 'chortkov', 'Дарахів': 'darakhov', 'Ковалівка': 'kovalyovka',
                          'Микулинці': 'mikulintsy', 'Хоростків': 'khorostkiv', 'Ланівці': 'lanovci',
                          'Товсте, Заліщицький район': 'tolstoe-ternopil-district', 'Устя-Зелене': 'ustye-zelenoe',
                          'Пробіжна': 'probezhnaya', 'Горинка': 'gorynka', 'Товсте, Гусятинський район': 'tolstoe',
                          'Гусятин': 'gusyatin', 'Заводське': 'zavodskoe', 'Доброполе': 'dobropole',
                          'Збараж': 'zbarazh', 'Яблунів': 'yablonov', 'Підволочиськ': 'podvolochisk',
                          'Зборів': 'zboriv', 'Білозірка': 'belozirka', 'Вишнівець': 'vishnevets',
                          'Бережани': 'berezhani', 'Підгайці': 'podgaytsi', 'Бучач': 'buchach',
                          'Млинівці, Кременецький район': 'mlinovci-ternopil-district', 'Козова': 'kozova',
                          'Завалів': 'zavalov', 'Дунаїв': 'dunayev', 'Великий Глибочок': 'veliky-glubochek',
                          'Джурин': 'jurin', 'Шумськ': 'shumsk', 'Золотники': 'zolotniky',
                          'Монастириська': 'monasturiska', 'Скалат': 'skalat', 'Почаїв': 'pochaev',
                          'Кременець': 'kremenets', 'Залізці': 'zalozhtsy', 'Копичинці': 'kopichintsi',
                          'Токи': 'toki', 'Скала-Подільська': 'scala-podolskaya', 'Дружба': 'drujba',
                          'Теребовля': 'terebovlya', 'Вишгородок': 'vyshgorodok', 'Коропець': 'koropets',
                          'Максимівка': 'maximovca', 'Борщівка': 'borshchovka', 'Іване-Пусте': 'ivane-puste',
                          'Куряни': 'curyany', 'Шумляни': 'shumlyany', 'Колодне': 'kolodnoe', 'Козлів': 'kozlov',
                          'Літятин': 'lityatin', 'Мельниця-Подільська': 'melnitsa-podolskaya'}

        self.html_pars = self.pars.get_html(self.dict_city['Тернопіль'])
        self.pars_data = self.pars.parse(self.html_pars)
        self.root_frame.grid_forget()
        self.root_frame = tkinter.Frame(self.root, width=1150, height=500, bg='#CFD8DC', bd=10)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)
        self.varp = tkinter.StringVar(self.root_frame)
        self.varp.set(self.ls_city[0])
        self.city_selectp = tkinter.OptionMenu(self.root_frame, self.varp, *self.ls_city)
        self.city_selectp.config(font='arial 14')
        self.pars_city_button = tkinter.Button(self.root_frame, font='arial 14', text='Прогноз погоди')


        self.name_city_labelp = tkinter.Label(self.root_frame, text=self.pars_data[0], font='arial 14', bg='#CFD8DC')
        self.weather_framep = tkinter.Frame(self.root_frame, bg='#ECEFF1')

        self.day_1_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][0], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_2_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][1], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_3_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][2], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_4_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][3], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_5_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][4], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_6_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][5], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_7_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][6], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_8_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][7], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_9_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][8], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')
        self.day_10_labelp = tkinter.Label(self.weather_framep, font='arial 12', text=self.pars_data[1][9], bg='#CFD8DC',
                                         justify='left', width=22, height=14, anchor='n')

        self.city_selectp.grid(row=0, column=1)
        self.pars_city_button.grid(row=0, column=2)
        self.name_city_labelp.grid(row=1, column=1, pady=20, padx=15)
        self.weather_framep.grid(row=2, column=0, columnspan=3, pady=15, padx=25)
        self.day_1_labelp.grid(row=0, column=0, pady=5, padx=5)
        self.day_2_labelp.grid(row=0, column=1, pady=5, padx=5)
        self.day_3_labelp.grid(row=0, column=2, pady=5, padx=5)
        self.day_4_labelp.grid(row=0, column=3, pady=5, padx=5)
        self.day_5_labelp.grid(row=0, column=4, pady=5, padx=5)
        self.day_6_labelp.grid(row=1, column=0, pady=5, padx=5)
        self.day_7_labelp.grid(row=1, column=1, pady=5, padx=5)
        self.day_8_labelp.grid(row=1, column=2, pady=5, padx=5)
        self.day_9_labelp.grid(row=1, column=3, pady=5, padx=5)
        self.day_10_labelp.grid(row=1, column=4, pady=5, padx=5)

        self.pars_city_button.bind('<Button-1>', self.pars_city)

    def pars_city(self, event):
        self.html_pars = self.pars.get_html(self.dict_city[self.varp.get()])
        self.pars_data = self.pars.parse(self.html_pars)
        self.name_city_labelp['text'] = self.pars_data[0]
        self.day_1_labelp['text'] = self.pars_data[1][0]
        self.day_2_labelp['text'] = self.pars_data[1][1]
        self.day_3_labelp['text'] = self.pars_data[1][2]
        self.day_4_labelp['text'] = self.pars_data[1][3]
        self.day_5_labelp['text'] = self.pars_data[1][4]
        self.day_6_labelp['text'] = self.pars_data[1][5]
        self.day_7_labelp['text'] = self.pars_data[1][6]
        self.day_8_labelp['text'] = self.pars_data[1][7]
        self.day_9_labelp['text'] = self.pars_data[1][8]
        self.day_10_labelp['text'] = self.pars_data[1][9]

    def api_frame(self, event):
        self.root_frame.grid_forget()
        self.root_frame = tkinter.Frame(self.root, width=1150, height=500, bg='#CFD8DC', bd=10)
        self.root_frame.grid(row=2, column=0, columnspan=3, padx=25)
        self.left_frame = tkinter.Frame(self.root_frame, width=200,bg='#CFD8DC', bd=10)
        self.left_frame.grid(row=0, column=0)
        self.right_frame = tkinter.Frame(self.root_frame, width=200,bg='#CFD8DC', bd=10)
        self.right_frame.grid(row=0, column=4)
        self.name_city_label = tkinter.Label(self.root_frame, text='Назва міста', font='arial 12', bg='#CFD8DC')
        self.name_city_entry = tkinter.Entry(self.root_frame, font='arial 14', bd=3)
        self.id_button = tkinter.Button(self.root_frame, width=25, text='Отримати ID міста.', font='arial 12')
        self.id_frame = tkinter.Frame(self.root_frame, bg='#CFD8DC')
        self.var = tkinter.StringVar(self.id_frame)
        self.city_select = tkinter.OptionMenu(self.id_frame, self.var, '')
        self.id_label = tkinter.Label(self.id_frame, font='arial 12', bg='#CFD8DC')
        self.weather_button = tkinter.Button(self.root_frame, width=25, text='Прогноз погоди / оновити.',
                                             font='arial 12')
        self.weather_frame = tkinter.Frame(self.root_frame, bg='#ECEFF1')
        self.day_1_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.day_2_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.day_3_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.day_4_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.day_5_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.day_6_label = tkinter.Label(self.weather_frame, font='arial 12', bg='#CFD8DC',
                                         justify='left', width=22, height=12, anchor='n')
        self.name_city_label.grid(row=0, column=1, pady=20, padx=15)
        self.name_city_entry.grid(row=0, column=2, pady=20, padx=15)
        self.id_button.grid(row=0, column=3, pady=20, padx=15)
        self.id_frame.grid(row=1, column=2)
        self.city_select.pack(side='left')
        self.id_label.pack()
        self.weather_button.grid(row=1, column=3)
        self.weather_frame.grid(row=2, column=1, columnspan=3, pady=15, padx=25)
        self.day_1_label.grid(row=0, column=0, pady=5, padx=5)
        self.day_2_label.grid(row=0, column=1, pady=5, padx=5)
        self.day_3_label.grid(row=0, column=2, pady=5, padx=5)
        self.day_4_label.grid(row=1, column=0, pady=5, padx=5)
        self.day_5_label.grid(row=1, column=1, pady=5, padx=5)
        self.day_6_label.grid(row=1, column=2, pady=5, padx=5)

        self.id_button.bind('<Button-1>', self.api_id)
        self.weather_button.bind('<Button-1>', self.api_weather)

    def api_id(self, event):
        self.name_city_ent = self.name_city_entry.get()
        self.id_name = self.owmapi.find_id(self.name_city_ent)
        self.city_select['menu'].delete(0, 'end')
        if len(self.id_name) > 0 and type(self.id_name) == dict:
            self.city_from_dict = tuple(self.id_name.keys())
            self.var.set(self.city_from_dict[0])
            for city in self.city_from_dict:
                self.city_select['menu'].add_command(label=city, command=tkinter._setit(self.var, city))

    def api_weather(self, event):
        self.id = self.id_name[self.var.get()]
        self.id_label['text'] = 'id:{}'.format(str(self.id))
        self.weather_str = self.owmapi.weather_forecast(self.id)
        self.day_1_label['text'] = self.weather_str[1][0]
        self.day_2_label['text'] = self.weather_str[1][1]
        self.day_3_label['text'] = self.weather_str[1][2]
        self.day_4_label['text'] = self.weather_str[1][3]
        self.day_5_label['text'] = self.weather_str[1][4]
        if len(self.weather_str[1]) == 6:
            self.day_6_label['text'] = self.weather_str[1][5]


class OpenweathermapAPI:
    """сайт http://openweathermap.org, дані по API."""

    def __init__(self):
        self.url_find = 'http://api.openweathermap.org/data/2.5/find'
        self.url_forecast = 'http://api.openweathermap.org/data/2.5/forecast'
        self.dict_id = dict()
        # self.city_country =
        self.appid = '1bb8b7a186b957c05745fd9c421fd44c'

    def find_id(self, city):
        """Знайти ID міста по назві.(назва міста і країна з бази сайта). """
        try:
            self.city = city
            self.dict_id.clear()
            self.parameters = {'q': city,  # Місто
                               'APPID': self.appid}  # API ключ
            self.r = requests.get(self.url_find, params=self.parameters)
            self.data_json = self.r.json()
            for i in range(len(self.data_json['list'])):
                self.city_id = self.data_json['list'][i]['id']  # ID міста
                self.city_country = '{} ({})'.format(self.data_json['list'][i]['name'],
                                                     self.data_json['list'][i]['sys']['country'])
                self.dict_id[self.city_country] = self.city_id
            return self.dict_id
        except Exception as e:
            return 'Exception (find_id):{}'.format(e)

    def weather_forecast(self, city_id):
        """Отримати погоду по id. """
        try:
            self.parameters = {'id': city_id,  # Місто
                               'units': 'metric',  # температури в одиницях градуси цельсія
                               'lang': 'uk',  # мова ( Ukrainian - uk (or ua))
                               'APPID': self.appid}  # API ключ
            self.r = requests.get(self.url_forecast, params=self.parameters)
            self.ls1 = []
            self.ls2 = []
            self.index = -1
            self.str_api = ''
            self.data_json = self.r.json()
            for i in self.data_json['list']:
                self.date = i['dt_txt'].split(' ')
                self.forecast = '{0} {1:+3.0f} {2}\n'.format(self.date[1][:5],
                                                             i['main']['temp'],
                                                             i['weather'][0]['description'])
                if self.date[0] in self.ls1:
                    self.str_api += self.forecast
                    self.ls2[self.index] += self.forecast
                else:
                    self.ls1.append(self.date[0])
                    self.index += 1
                    self.ls2.insert(self.index, '\n{0:^14}\n\n'.format(self.date[0]))
                    self.ls2[self.index] += self.forecast
                    self.str_api += '\n{0:^14}\n\n'.format(self.date[0])
                    self.str_api += self.forecast
            return self.str_api, self.ls2
        except Exception as e:
            return 'Exception (weather_forecast):{}'.format(e)


class YandexWeatherParse:
    """сайт https://yandex.ua/pogoda/ternopol, Парсинг."""

    def __init__(self):

        self.str_parse = ''
        self.ls_days = []
        self.ls_days2 = []

    def get_html(self, city):
        """Отримати HTML сторінку. """
        try:
            self.city = city
            self.url = 'https://yandex.ua/pogoda/{}/details'.format(self.city)
            response = requests.get(self.url)
            return response.text
        except Exception as e:
            return 'Exception (get_html):{}'.format(e)

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
                self.str_parse += '{0:^22}\n'.format(self.ls_days[i])
                self.ls_days2.insert(i, '{0:^22}\n'.format(self.ls_days[i]))
                row = value.find_all('tr', 'weather-table__row')
                for day_part in row:
                    day_part_name = day_part.find('div', 'weather-table__daypart')
                    day_part_name = day_part_name.text
                    day_part_t = day_part.find('div', 'weather-table__temp')
                    day_part_t = day_part_t.text
                    day_part_v_td = day_part.find('td', 'weather-table__body-cell_type_condition')
                    day_part_v = day_part_v_td.find('div', 'weather-table__value')
                    day_part_v = day_part_v.text
                    day_part_str = '{0:<11}{1:^11}\n{2:<22}'.format(day_part_name, day_part_t, day_part_v)
                    self.str_parse += '{}\n'.format(day_part_str)
                    self.ls_days2[i] += '\n{}\n'.format(day_part_str)
            return self.head.text, self.ls_days2
        except Exception as e:
            return 'Exception (parse):{}'.format(e)


owmapi = OpenweathermapAPI()
pars = YandexWeatherParse()
window_root = Window(owmapi, pars)
