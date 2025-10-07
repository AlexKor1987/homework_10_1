from unittest.mock import mock_open, patch
import pytest
from src.csv_xlsx import open_file_csv, open_file_excel


@patch('builtins.open', new_callable=mock_open, read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации')
def test_open_file_csv(mock_open):
    expected_result = [
        {
            'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result


@patch('builtins.open', new_callable=mock_open, read_data=None)
def test_open_file_csv_file_empty(mock_open):
    expected_result = []
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result


@patch('builtins.open', new_callable=mock_open, read_data="Nothing")
def test_open_file_csv_not_file(mock_open):
    expected_result = []
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result


@patch('builtins.open', new_callable=mock_open, read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации')
def test_open_file_excel(mock_open):
    expected_result = [
        {
            'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result


@patch('builtins.open', new_callable=mock_open, read_data=None)
def test_open_file_excel_file_empty(mock_open):
    expected_result = []
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result


@patch('builtins.open', new_callable=mock_open, read_data="Nothing")
def test_open_file_excel_not_file(mock_open):
    expected_result = []
    result = open_file_csv('fake/path/to/file.csv')
    assert result == expected_result
