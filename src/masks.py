import logging
from typing import AnyStr

# os.makedirs('logs', exist_ok=True) #Создание папки  "logs", если её не существует
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    "C:/Users/PB/Desktop/Python/homework_10_1/logs/masks.log",
    mode="w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    counter = 0
    result_card_number = ""
    temp_card_number = []
    logger.debug(f"Попытка маскировки номера банковской карты: {card_number}")

    if len(str(card_number)) != 16:
        logger.error("Неверный номер банковской карты")
        raise ValueError("Неверный номер банковской карты")
    if int(card_number) == 0:
        logger.error("Неверный номер банковской карты")
        raise ValueError("Неверный номер банковской карты")
    if not str(card_number).isdigit():
        logger.error("Неверный номер банковской карты")
        raise ValueError("Неверный номер банковской карты")
    for number in str(card_number):
        counter += 1
        if 6 < counter <= len(str(card_number)) - 4:
            temp_card_number.append("*")
        else:
            temp_card_number.append(number)
    res_1 = temp_card_number[:4]
    res_2 = temp_card_number[4:8]
    res_3 = temp_card_number[8:12]
    res_4 = temp_card_number[12:16]
    result_card_number = (
        "".join(res_1)
        + " "
        + "".join(res_2)
        + " "
        + "".join(res_3)
        + " "
        + "".join(res_4)
    )
    logger.debug(f"Маскировка номера банковской карты {card_number} прошла успешно")
    return result_card_number


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    counter = 0
    temp_account_number = []
    logger.debug(f"Попытка маскировки номера банковского счета: {account_number}")

    if len(str(account_number)) < 19:
        logger.error("Неверный номер банковского счета")
        raise ValueError("Неверный номер банковского счета")
    if int(account_number) == 0:
        logger.error("Неверный номер банковского счета")
        raise ValueError("Неверный номер банковского счета")
    if not str(account_number).isdigit():
        logger.error("Неверный номер банковского счета")
        raise ValueError("Неверный номер банковского счета")
    for number in str(account_number):
        counter += 1
        if counter <= len(str(account_number)) - 4:
            temp_account_number.append("*")
        else:
            temp_account_number.append(number)
    result_card_number = temp_account_number[14:]
    logger.debug(f"Маскировка номера банковского счета {account_number} прошла успешно")
    return "".join(result_card_number)


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print("".join(get_mask_account(73654108430135874305)))
