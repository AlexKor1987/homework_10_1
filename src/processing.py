'''В модуле processing напишите функцию filter_by_state, которая принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.'''
from typing import Dict, List

def filter_by_state(list_of_id: list[Dict],
                    state: str = "EXECUTED") -> list[Dict]:
    new_list_of_id = []
    for number in range(len(list_of_id)):
        if list_of_id[number]["state"] == state:
            new_list_of_id.append(list_of_id[number])
        # print(list_of_id[number])
    #print(new_list_of_id)
    return new_list_of_id
if __name__ == "__main__":
    dict_data = [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    print(filter_by_state((dict_data), state = "CANCELED"))




'''
В том же модуле напишите функцию sort_by_date, которая принимает список словарей и необязательный параметр, задающий
порядок сортировки(по умолчанию — убывание).Функция должна возвращать новый список, отсортированный по дате(date).
'''