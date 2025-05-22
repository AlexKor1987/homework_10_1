from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_card: str) -> str:
    """Функция обрабатывающая информацию как о картах, так и о счетах."""
    info_card_list = info_card.split()
    if len(str(info_card_list[-1])) < 16:
        raise ValueError ('Неверный номер счета/карты')
    if int(info_card_list[-1]) == 0:
        raise ValueError ('Неверный номер счета/карты')
    if not str(info_card_list[-1]).isdigit():
        raise ValueError ('Неверный номер счета/карты')
    if "Счет" in info_card_list:
        #return f"Счет **{info_card_list[-1][-4:]}"
        return f"Счет {get_mask_account(info_card_list[1])}"
    else:
        card_name = " ".join(info_card_list[:-1])
        card_number = info_card_list[-1].replace(" ", "")
        return f"{card_name} {get_mask_card_number(card_number)}"


def get_date(date: str) -> str:
    """Функция смены формата даты"""
    date_time = datetime.fromisoformat(date)
    print(date_time)
    if int(date_time.strftime("%d")) > 31:
        raise ValueError ('Неверное число месяца')
    if int(date_time.strftime("%m")) > 12:
        raise ValueError ('Неверный месяц года')
    if str(date_time) == 0:
        raise ValueError ('Отсутствует дата')
    formatted_date = date_time.strftime("%d.%m.%Y")
    return formatted_date


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 3538303347444789556"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
