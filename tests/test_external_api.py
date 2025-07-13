from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub(mock_get):  # Тестируем конвертацию валюты
    mock_get.return_value.json.return_value = {"result": 1}
    mock_get.return_value.status_code = 200
    transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
    result = convert_to_rub(transaction)
    assert result == 1
