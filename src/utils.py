import json


def open_file(path: str) -> list:
    """Функция открытия файла - путь файла передается в эту функцию"""
    with open(path, encoding='utf-8') as json_file:
        book_info = json.load(json_file)
        #print(book_info) # data - словарь, тип dict
        # #print(type(book_info))
    return book_info


if __name__ == "__main__":
    open_file('C:/Users/PB/Desktop/Python/homework_10_1/data/operations.json')
