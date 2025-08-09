import json
from typing import Any, Dict, List
from unittest.mock import patch
import logging
import os


logger = logging.getLogger('utils')
file_handler = logging.FileHandler('C:/Users/PB/Desktop/Python/homework_10_1/logs/utils.log', mode="w", encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

#os.makedirs('logs', exist_ok=True) #Создание папки  "logs", если её не существует
#logger = logging.getLogger("utils")
#logger.setLevel(logging.DEBUG)
#file_handler = logging.FileHandler(logs/utils.log', mode="w", encoding='utf-8')
#file_handler.setLevel(logging.DEBUG)
#file_formatter = logging.Formatter('%(asctime)s %(levelname)s: $(message)s')
#file_handler.setFormatter(file_formatter) #FileHandler - используется для вывода логов в файл


def open_file_get_transactions(file_path: str) -> list[Dict[str, Any]]:
    """Функция открытия файла - принимает на вход путь до json - файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        logger.debug(f"Попытка загрузить файл: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data_json = json.load(file)
            if isinstance(data_json, list):
                logger.debug(f"Файл: {file_path} успешно загружен")
                return data_json
    except FileNotFoundError:
        logger.error(f"Файл: {file_path} не найден")
        return []
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []


if __name__ == "__main__":
    print(
        open_file_get_transactions(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json"
        )
    )











