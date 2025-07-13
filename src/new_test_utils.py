def test_load_transactions_valid_json(mocker):

    # Создаем тестовые данные

    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    mock_open = mock.mock_open(read_data=json.dumps(test_data))

    # Патчим open в builtins, чтобы использовать наш mock_open

    with mock.patch("builtins.open", mock_open):

        result = load_transactions("fake_path.json")

        assert result == test_data





@patch('requests.get')
                def test_convert_to_rub(mock_get: Mock):  # Тестируем конвертацию валюты
                    mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}
                    transaction = {'amount': 100, 'currency': 'USD'}
                    result = convert_to_rub(transaction)
                    assert result == 7500.0





