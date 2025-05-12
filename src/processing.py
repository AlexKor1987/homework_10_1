# from typing import Dict, List


def filter_by_state(list_of_id: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально
    значение для ключа state (по умолчанию 'EXECUTED'). Функция
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    new_list_of_id = []
    for number in range(len(list_of_id)):
        if list_of_id[number]["state"] == state:
            new_list_of_id.append(list_of_id[number])
    return new_list_of_id


def sort_by_date(list_of_id: list, reverse_date: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный
    параметр, задающий порядок сортировки(по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате(date)."""
    sorted_by_date = []
    sorted_by_date = sorted(
        list_of_id, key=lambda list_of_id: list_of_id["date"], reverse=reverse_date
    )
    return sorted_by_date


if __name__ == "__main__":
    dict_data = [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    print(filter_by_state((dict_data), state="CANCELED"))
    print(sort_by_date((dict_data), reverse_date=False))
