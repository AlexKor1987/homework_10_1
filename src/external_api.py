import os
from dotenv import load_dotenv
import requests
import json
from typing import Any, Dict, Generator, Iterator, List
from src.utils import open_file_get_transactions
from unittest.mock import Mock
from unittest.mock import patch
#from tests.test_generators import transactions


def convert_to_rub(transaction):
  """Функция конвертации валюты (принимает на вход транзакцию и возвращает сумму транзакуций
  (amount) в рублях, тип данных "float". Если транзакция была а "USD" или "EUR" происходит
  обращение к внешнему API"""
  operation_amount = transaction.get("operationAmount", {})
  amount = operation_amount.get("amount", 0)
  currency_code = operation_amount.get("currency", {}).get("code", 0)
  if currency_code == "RUB":
    return amount
  elif currency_code == "USD" or currency_code == "EUR":
    load_dotenv()  # Загрузка переменных из .env-файла
    apikey = os.getenv('API_KEY')  # Получение значения переменной API_KEY из .env-файла
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {
      "apikey": apikey
    }
    try:
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
        return float(response.json()['result'])
      else:
        return None
    except requests.exception.RequestException as error:
      print ("Failed to get currency rate ", error)
      return 0.0


if __name__ == "__main__":
  transactions = open_file_get_transactions('C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json')
  for transaction in transactions:
    convert_to_rub(transaction)


# Для проверки без использования API
  dict1 =   {
     "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }

  #print(convert_to_rub(dict1))
