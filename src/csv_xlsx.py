import csv
import pandas as pd
from typing import Any, Dict


def open_file_csv(file_path: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых операций из CSV - файла,
    принимает путь к файлу CSV в качестве аргумента и выдает список
    словарей с транзакциями.
    Если файл пустой, содержит не список или не найден, функция возвращает
    пустой список.
    """
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter = ';')
            result = []
            for row in reader:
                result.append(row)
        return result

    except FileNotFoundError:
        return []
    except Exception as e:
        return []


def open_file_excel(file_path: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых операций из Excel - файла,
    принимает путь к файлу Excel в качестве аргумента и выдает список
    словарей с транзакциями.
    Если файл пустой, содержит не список или не найден, функция возвращает
    пустой список. Значения столбцов 'id' и 'amount' были в формате 'float'?
    они преобразовались в формат 'int' с помощью 'astype(int)'
    """
    try:
        df = pd.read_excel(file_path)
        df[['id', 'amount']] = df[['id', 'amount']].astype(int)
        result = df.to_dict(orient= 'records')
        return result

    except FileNotFoundError:
        return []
    except Exception as e:
        return []


if __name__ == "__main__":
    print(
        open_file_csv(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/transactions.csv"
        )
    )

    print(
        open_file_excel(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/transactions_excel.xlsx"
        )
    )

# from unittest.mock import patch, Mock
#
#
# @patch('your_module.pd.read_csv')
# def test_your_function(mock_read_csv):
#     # Создаем объект Mock
#     mock_data = Mock()
#     mock_read_csv.return_value = mock_data
#
#     # Теперь вызываем твою функцию
#     result = your_function('path_to_file.csv')
#
#     # Проверяем, что функции были вызваны корректно
#     mock_read_csv.assert_called_once_with('path_to_file.csv')