from json import load, dump
from pprint import pprint

with open('vacancies_dict', 'r') as full_dict:
    dict_for_print = load(full_dict)

# pprint(type(dict_for_print['35269923']['skills']))


skills_string = ''

# for each_value in dict_for_print.values():
#     for each_skill in each_value['skills']:
#         skills_string += '{}, '.format(each_skill['name'])
#     # skills_string += f'{skills_string[-1]} \n'
#     #     skills_string = skills_string[-1]
#     skills_string += '\n'
# print(skills_string)


dict_for_html = {}

vacancies_list_for_index = list(dict_for_print.values())


vacancy_string = ''
# skills_string = ''

for each_value in dict_for_print.values():
    vacancy_string = ''
    url_string = '<a href="{}"</a>'.format(each_value['url'])
    vacancy_string += f'{url_string}\n'

    skills_string = ''
    if len(each_value['skills']) != 0:
        for each_skill in each_value['skills']:
            skills_string += '{}, '.format(each_skill['name'])

    else:
        skills_string = 'Навыки не указаны  '
    skills_string = skills_string[:-2]
    skills_string += '\n'

    if each_value['salary'] is not None:
        if each_value['salary']['from'] is not None and each_value['salary']['currency'] == 'RUR':
            salary_string = 'Зарплата - {}'.format(each_value['salary']['from'])
            vacancy_string += f'{salary_string}\n'
        else:
            salary_string = 'Зарплата не указана'
            vacancy_string += f'{salary_string}\n'
    else:
        salary_string = 'Зарплата не указана'
        vacancy_string += f'{salary_string}\n'

    vacancy_string += f'{skills_string}\n'

    vacancy_index = vacancies_list_for_index.index(each_value) + 1

    dict_for_html[vacancy_index] = vacancy_string


with open('vacancies_for_html', 'w') as f:
    dump(dict_for_html, f)


pprint(dict_for_html)