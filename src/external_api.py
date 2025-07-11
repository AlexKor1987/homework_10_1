
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
#  result = response.json()
#  parsed_data = json.loads(result)
#  print(parsed_data)
  result = response.text

  print(result)




def exchange_rates(book_info: list) -> list:
  print(book_info)






if __name__ == "__main__":
 # convert_to_rub("USD", 10)
  exchange_rates(open_file('C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json'))






