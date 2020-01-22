import requests
import pprint
import json
import time
import sys


class HHRequests:

    # создаем конструктор класса
    def __init__(self, vacancy_text, vacancy_town):
        self._vacancy_text = vacancy_text
        self._vacancy_town = vacancy_town

    # создаем функцию для доступа к переменной self._vacancy_text
    @property
    def vacancy_text(self):
        return self._vacancy_text

    # создаем функцию для доступа к переменной self._vacancy_town
    @property
    def vacancy_town(self):
        return self._vacancy_town

    # создаем функцию для соединения
    @property
    def hh_connector(self):

        # создаем переменную для сайта с api
        hh_url = 'https://api.hh.ru/'

        # создаем переменную для полного пути к вакансиям
        hh_url_vacancies = f'{hh_url}vacancies'

        # создаем переменную для полного пути к справочнику городов
        hh_url_areas = f'{hh_url}suggests/areas'

        # формируем запрос к справочнику городов по условию 'название города'
        hh_area_id_response = requests.get(hh_url_areas,
                                           params={'text': self.vacancy_town}
                                           ).json()

        # из справочника городов по условию 'название города' получаем id этого города
        # 0 - это Россия, пока не реализовал поиск для других стран
        area_id = hh_area_id_response['items'][0]['id']

        # создаем строку параметров для запроса вакансий по условиям 'текст вакансии', 'id города'
        hh_connection_params = {
                                'text': self.vacancy_text,
                                'area': area_id,
                                'page': 1
                                }
        # формируем запрос для запроса информации о вакансиях по условиям 'текст вакансии', 'id города'
        hh_response = requests.get(hh_url_vacancies,
                                   params=hh_connection_params
                                   ).json()
        return hh_response

    # функция для запроса информации о вакансиях и сохранения информации в файл json-формата
    @property
    def hh_get_vacancy_inf(self):

        # соединяемся с api.hh.ru/vacancies
        hh_response = self.hh_connector

        # создаем пустой словарь для сохранения информации о скачанных вакансиях
        vacancies_dict = {}

        # создаем цикл для постраничного скачивания вакансий с api.hh.ru/vacancies и
        # постранично (20 вакансий на странице) скачиваем вакансии
        for page_number in range(0, 2):

            # из-за ограничения api.hh.ru/vacancies, вводим искуственную задержку
            # отсчитываем в терминале 3-х секундные интервалы
            for vacancy in hh_response['items']:

                time.sleep(2)

                # скачиваем информацию о вакансии и сохраняем ее в словарь
                current_response = requests.get(vacancy['url']).json()
                vacancies_dict[vacancy['id']] = {'url': vacancy['alternate_url'],
                                                 'skills': current_response['key_skills'],
                                                 'salary': current_response['salary']
                                                 }
            # выводим в терминал сообщение о скачивании одной страницы с вакансиями (20 шт.)
            sys.stdout.write(f'\nВакансии со страницы {page_number+1} загружены!\n')

            # каждую страницу с вакансиями сохраняем в файл формата json
            with open('vacancies_dict', 'w') as f:
                json.dump(vacancies_dict, f)
        return vacancies_dict


if __name__ == '__main__':
    test_connector = HHRequests('python', 'Санкт-Петербург')
    pprint.pprint(test_connector.hh_get_vacancy_inf)