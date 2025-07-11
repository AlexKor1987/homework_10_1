
import os
from dotenv import load_dotenv
import requests
import json
from typing import Any, Dict, Generator, Iterator, List
from src.utils import open_file


def convert_to_rub(currency_not_rub: str, amount_not_rub: float) -> float:
  """Функция конвертации валюты"""
  load_dotenv() # Загрузка переменных из .env-файла
  apikey = os.getenv('API_KEY') # Получение значения переменной API_KEY из .env-файла
  url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_not_rub}&amount={amount_not_rub}"
  payload = {}
  headers= {
    "apikey": apikey
  }
  response = requests.request("GET", url, headers=headers, data = payload)
  if response.status_code != 200:#
    raise ValueError(f"Failed to get currency rate")#
  status_code = response.status_code
  result = response.text
  parsed_result = json.loads(result) #преобразование строки JSON в объект Python
  print(result)
  print(parsed_result["result"]) # Получаем значение словаря по ключу
  return parsed_result["result"]


def exchange_rates(book_info: list) -> list[list[Any] | Any]:
  """Функция принимаеющая на вход транзакцию и возвращаещая сумму транзакции в рублях"""
  new_book_info = []
  if len(book_info) == 0:
    raise ValueError("Пустой список")
 # for i in book_info:
 #   if (
 #           i["operationAmount"]["currency"]["code"] != "USD"
 #           and i["operationAmount"]["currency"]["code"] != "RUB"
 #   ):
 #     raise ValueError("Неверная валюта")
  for i in book_info:
    if 'operationAmount' in i and i['operationAmount']['currency']['code'] == 'RUB':
      new_book_info.append(i)
    if 'operationAmount' in i and i['operationAmount']['currency']['code'] != 'RUB':
      currency = i['operationAmount']['currency']['code']
      amount = i['operationAmount']['amount']
      i['operationAmount']['currency']['code'] = 'RUB'
      i['operationAmount']['currency']['name'] = 'руб.'
      i['operationAmount']['amount'] = convert_to_rub(currency, amount)
      new_book_info.append(i)
  with open('C:/Users/PB/Desktop/Python/homework_10_1/data/new_operations.json', 'w', encoding='utf-8') as f:
    json.dump(book_info, f)

  print(new_book_info)
  return new_book_info








if __name__ == "__main__":
  convert_to_rub("USD", 11,999)
  #exchange_rates(open_file('C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json'))








