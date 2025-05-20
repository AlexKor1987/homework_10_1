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


def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number('7000792289606361') == card_numbers


def test_get_mask_account(mask_accounts):
    assert get_mask_account('73654108430135874305') == mask_accounts


def test_filter_by_state(by_state):
    assert filter_by_state((dict_data), state="CANCELED") == by_state


def test_sort_by_date(by_date):
    assert sort_by_date((dict_data), reverse_date=False) == by_date


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


def test_get_date(getting_date):
    assert get_date('2024-03-11T02:26:18.671407') == getting_date

