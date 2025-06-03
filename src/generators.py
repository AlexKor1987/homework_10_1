from typing import List, Dict, Any, Iterator, Generator

def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция фильтрации транзакции по заданной валюте, возвращает итератор."""
    if len(transactions_list) == 0:
        raise ValueError('Пустой список')
    for i in transactions_list:
        if i["operationAmount"]["currency"]["code"] != "USD" and i["operationAmount"]["currency"]["code"] != "RUB":
            raise ValueError('Неверная валюта')
    for i in transactions_list:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    if len(transactions_list) == 0:
        raise ValueError('Пустой список')
    for i in transactions_list:
         if i["description"] != "Перевод организации" and i["description"] != "Перевод со счета на счет" and i["description"] != "Перевод с карты на карту":
            raise ValueError('Неверное описание операции')
    for i in transactions_list:
        yield i["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне"""
    if stop < start:
        raise ValueError('Неверный диапазон номеров карт')
    if start < 0:
        raise ValueError('Неверный начальный диапазон номеров карт')
    if stop <= 0:
        raise ValueError('Неверный конечный диапазон номеров карт')
    if start == 0 and stop == 0:
        raise ValueError('Нулевой диапазон номеров карт')
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

    #gen = filter_by_currency(transactions, 'RUB')
    #try:
    #    print(next(gen))
    #    print(next(gen))
    #    print(next(gen))
    #except StopIteration:
    #    print('Больше нет транзакций в этой валюте')

#    usd_transactions = list(filter_by_currency(transactions, "USD"))
#    print(usd_transactions[:4])

    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(3):
        print(next(usd_transactions))





#    trans = transaction_descriptions(transactions)
    descriptions = transaction_descriptions(transactions)
    for i in range(5):
        print(next(descriptions))

#    try:
#        print(next(trans))
#        print(next(trans))
 #       print(next(trans))
#        print(next(trans))
#        print(next(trans))
 #   except StopIteration:
#        print('Больше нет транзакций')





    for card_number in card_number_generator(1, 5):
        print(card_number)