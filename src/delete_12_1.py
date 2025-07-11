
import json

from src.utils import load_transactions

# Путь к файлу operations.json
file_path = 'data/operations.json'

with open(file_path) as f:
    operations = json.load(f)

transactions = load_transactions(file_path)

if transactions:
    print("Загруженные транзакции:")
    for transaction in transactions:
        print(transaction)
else:
    print("Нет доступных транзакций или файл пуст.")