import csv



def open_file_csv(file_path: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых операций из CSV - файла,
    принимает путь к файлу CSV в качестве аргумента и выдает список
    словарей с транзакциями.
    Если файл пустой, содержит не список или не найден, функция возвращает
    пустой список.
    """
    import    try:
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


def open_file_excel(file_path: str) -> list[Dict[str, Any]]:
    """Функция для считывания финансовых операций из Excel - файла,
    принимает путь к файлу Excel в качестве аргумента и выдает список
    словарей с транзакциями.
    Если файл пустой, содержит не список или не найден, функция возвращает
    пустой список.
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
        open_file_csv(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/transactions.csv"
        )
    )

    print(
        open_file_excel(
            "C:/Users/PB/Desktop/Python/homework_10_1/data/transactions_excel.xlsx"
        )
    )


