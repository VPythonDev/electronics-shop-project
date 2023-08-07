"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def smartphone():
    return Item("Смартфон", 15000, 10)


def test_calculate_total_price(smartphone):
    assert smartphone.calculate_total_price() == 150000


def test_apply_discount(smartphone):
    Item.pay_rate = 0.5
    assert smartphone.apply_discount() == 7500


def test_repr(smartphone):
    assert repr(smartphone) == "Смартфон, цена: 15000, кол-во: 10"
