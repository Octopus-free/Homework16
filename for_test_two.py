import  json
import pprint

test_dict = {
    '1': 'abc',
    '2': 'def'
}

# test_list = list(test_dict.values())
# print(type(test_list))

for each_value in test_dict.keys():
    print(f'Ключ: {each_value}, значение {test_dict[each_value]})')

# print(test_list)

with open('vacancies_for_html', 'r') as vac_dict:
    full_dict = json.load(vac_dict)

    pprint.pprint(full_dict)


