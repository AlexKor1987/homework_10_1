import json
from typing import Any, Dict, List
from unittest.mock import patch


def open_file_get_transactions(file_path: str) -> list[Dict[str, Any]]:
    """Функция открытия файла - принимает на вход путь до json - файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data_json = json.load(file)
            if isinstance(data_json, list):
                return data_json
    except:
        return []


if __name__ == "__main__":
    print(
        open_file_get_transactions(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json"
        )
    )
