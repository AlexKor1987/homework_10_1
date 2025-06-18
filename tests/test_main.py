import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date


dict_data = [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]



# get_mask_card_number
def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number('7000792289606361') == card_numbers


def test_get_mask_card_number_invalid_number(card_numbers):
    with pytest.raises(ValueError):
        get_mask_card_number('70007922896063611')


def test_get_mask_card_number_zero_number(card_numbers):
    with pytest.raises(ValueError):
        get_mask_card_number('0000000000000000')


def test_get_mask_card_number_no_digit_number(card_numbers):
    with pytest.raises(ValueError):
        get_mask_card_number('70007ABC89606361')


@pytest.mark.parametrize("value, expected", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('7000792289606360', '7000 79** **** 6360'),
    ('7000792289606359', '7000 79** **** 6359'),
    ('7000792289606459', '7000 79** **** 6459'),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


# get_mask_account
def test_get_mask_account(mask_accounts):
    assert get_mask_account('73654108430135874305') == mask_accounts


def test_get_mask_account_invalid_number(card_numbers):
   with pytest.raises(ValueError):
       get_mask_account('736541084301358743')


def test_get_mask_account_zero_number(card_numbers):
    with pytest.raises(ValueError):
        get_mask_account('00000000000000000000')


def test_get_mask_account_no_digit_number(card_numbers):
    with pytest.raises(ValueError):
        get_mask_account('7ABC4108430135874305')


@pytest.mark.parametrize("value, expected", [
    ('73654108430135874305', '**4305'),
    ('73654108430135874303', '**4303'),
    ('73654108430135874300', '**4300'),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


# filter_by_state
def test_filter_by_state(by_state):
    assert filter_by_state((dict_data), state="CANCELED") == by_state


def test_filter_by_state_bad_state(by_state):
    with pytest.raises(ValueError):
        filter_by_state((dict_data), state="CANC")


@pytest.mark.parametrize('value, state, expected', [
    ((dict_data), "CANCELED", [
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]),
    ((dict_data), "EXECUTED", [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
   ])
def test_filter_by_state(value, state, expected):
    assert filter_by_state(value, state) == expected


# sort_by_date
def test_sort_by_date(by_date):
    assert sort_by_date((dict_data), reverse_date=False) == by_date


def test_sort_by_date_bad_month(by_date):
   with pytest.raises(ValueError):
       sort_by_date([
        {"id": 615064591, "state": "CANCELED", "date": "2018-15-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ], reverse_date=False)


def test_sort_by_date_bad_day(by_date):
   with pytest.raises(ValueError):
       sort_by_date([
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-33T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ], reverse_date=False)


def test_sort_by_date_bad_date(by_date):
   with pytest.raises(ValueError):
       sort_by_date([], reverse_date=False)


@pytest.mark.parametrize('value, reverse_date, expected', [
    ((dict_data), False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
((dict_data), True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
   ])
def test_sort_by_date(value, reverse_date, expected):
    assert sort_by_date(value, reverse_date) == expected


# mask_account_card
def test_mask_account_card(account_cards):
    assert mask_account_card('Maestro 1596837868705199') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('Счет 64686473678894779589') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('MasterCard 7158300734726758') == account_cards



def test_mask_account_card(account_cards):
    assert mask_account_card('Счет 3538303347444789556') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('Visa Classic 6831982476737658') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('Visa Platinum 8990922113665229') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('Visa Gold 5999414228426353') == account_cards


def test_mask_account_card(account_cards):
    assert mask_account_card('Счет 73654108430135874305') == account_cards


def test_mask_account_card_invalid_number(account_cards):
   with pytest.raises(ValueError):
       mask_account_card('Счет 353830334744')


def test_mask_account_card_zero_number(account_cards):
    with pytest.raises(ValueError):
        mask_account_card('0000000000000000')


def test_mask_account_card_no_digit_number(account_cards):
   with pytest.raises(ValueError):
       mask_account_card('Visa Gold 5ABC414228426353')


@pytest.mark.parametrize("value, expected", [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 3538303347444789556', 'Счет *9556'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305'),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


# get_date
def test_get_date(getting_date):
    assert get_date('2024-03-11T02:26:18.671407') == getting_date


def test_get_date(getting_date):
   with pytest.raises(ValueError):
       get_date('2024-03-33T02:26:18.671407')


def test_get_date(getting_date):
   with pytest.raises(ValueError):
       get_date('2024-13-11T02:26:18.671407')


def test_get_date(getting_date):
   with pytest.raises(ValueError):
       get_date('0')


@pytest.mark.parametrize("value, expected", [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-04-11T02:26:18.671407', '11.04.2025'),
    ('2025-05-15T02:26:18.671407', '15.05.2025'),
])
def test_get_date(value, expected):
    assert get_date(value) == expected

