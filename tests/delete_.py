from unittest.mock import patch
import pytest
import pandas as pd
from src.csv_xlsx import open_file_csv, open_file_excel




@pytest.fixture
def two_transactions() -> list:
    return [
        {
            'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        },
        {
            'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
            'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'
        }
    ]


''' Тест функции reading_cvs '''

#@patch('open_file_csv')
#@patch('__main__.open_file_csv')
@patch('builtins.open')
def test_open_file_csv(mock_open_file) -> None:
    mock_open_file_return_value = [
        {
            'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        },
        {
            'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
            'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'
        }
    ]
    pd.DataFrame(mock_open_file_return_value)
    mock_open_file.return_value = pd.DataFrame(mock_open_file_return_value)
    data_csv = "C:/Users/PB/Desktop/Python/homework_10_1/data/transactions.csv"
    assert open_file_csv(data_csv) == [
        {
            'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        },
        {
            'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
            'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'
        }
    ]
    #mock_open_file.assert_called_once_with(data_csv)