from typing import AnyStr


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    counter = 0
    result_card_number = ""
    temp_card_number = []
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
    result_card_number = "".join(res_1) + " " + "".join(res_2) + " " + "".join(res_3) + " " + "".join(res_4)
    return result_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    counter = 0
    temp_account_number = []
    for number in str(account_number):
        counter += 1
        if counter <= len(str(account_number)) - 4:
            temp_account_number.append("*")
        else:
            temp_account_number.append(number)
    result_card_number = temp_account_number[14:]
    return "".join(result_card_number)


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print("".join(get_mask_account(73654108430135874305)))

