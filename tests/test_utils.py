from unittest.mock import patch
from src.utils import open_file_get_transactions
import json

@patch('builtins.open', create=True)
def test_open_file_get_transactions(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = '[]'
    assert open_file_get_transactions('test.txt') == []
    mock_open.assert_called_once_with('test.txt', 'r', encoding='utf-8')