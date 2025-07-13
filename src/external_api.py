import json
import os
from typing import Dict, List

import requests
from dotenv import load_dotenv

from src.utils import open_file_get_transactions

EXCHANGE_RATES_API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты (принимает на вход транзакцию и возвращает сумму транзакуций
    (amount) в рублях, тип данных "float". Если транзакция была а "USD" или "EUR" происходит
    обращение к внешнему API"""
    amount = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]
    if currency_code == "RUB":
        return float(amount)
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": amount}
    headers = {"apikey": EXCHANGE_RATES_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])


if __name__ == "__main__":
    transactions = open_file_get_transactions(
        "C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json"
    )
    for transaction in transactions:
        convert_to_rub(transaction)

    # Для проверки без использования API
    dict1 = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }

# print(convert_to_rub(dict1))
