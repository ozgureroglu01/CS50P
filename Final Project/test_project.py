from project import get_convert_from, get_convert_to, convert
import pytest


def test_get_convert_from():
    assert get_convert_from("USA") == "USD"
    assert get_convert_from("Germany") == "EUR"

def test_get_convert_to():
    assert get_convert_to("USA") == "USD"
    assert get_convert_to("Germany") == "EUR"


def test_convert():
    assert convert("USD","EUR",1) == 0.92
