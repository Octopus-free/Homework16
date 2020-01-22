from flask import Flask, render_template, request
from hh_request import HHRequests
import json
from parser_json_dict import  ParserJsonDict
import pprint


# инициализруем оъект Flask
hh_parser_site = Flask(__name__)


@hh_parser_site.route("/", methods=['GET'])
def hh_site():
    return render_template('hh_site.html')


@hh_parser_site.route("/vacancies", methods=['GET'])
def hh_request():
    full_dict = {}
    return render_template('hh_request.html', data = full_dict)


@hh_parser_site.route("/vacancies", methods=['POST'])
def hh_request_post():
    print('post')

    # создаем переменную для хранения текста (описания вакансии) запроса
    # пользователя к hh.ru
    hh_request_text = request.form['vacancy_text']

    # создаем переменную для хранения города в запросе
    # пользователя к hh.ru
    hh_request_town = request.form['vacancy_town']

    # создаем экземпляр класса HHRequests
    # передавая ему, введенные пользователем данные
    hh_response = HHRequests(hh_request_text, hh_request_town)

    # создаем словарь, содержащий данные о вакансиях с hh.ru
    # вызывая метод hh_get_vacancy_inf
    # full_dict = hh_response.hh_get_vacancy_inf

    with open('vacancies_for_html', 'r') as vac_dict:
        full_dict = json.load(vac_dict)

    pprint.pprint(full_dict)

    return render_template('hh_request.html', data=full_dict)



@hh_parser_site.route("/contacts", methods=['GET'])
def hh_contacts():
    return render_template('hh_contacts.html')


if __name__ == '__main__':
    hh_parser_site.run(debug=True)