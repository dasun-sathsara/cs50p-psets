from fuel import convert, guage
import pytest


def test_convert_zero_division():
    pytest.raises(ZeroDivisionError, convert, "2/0")


def test_convert_value_error():
    pytest.raises(ValueError, convert, "2/l")
    pytest.raises((ValueError), convert, "5/3")


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/5") == 20
    assert convert("5/20") == 25


def test_guage_e():
    assert guage(0) == "E"
    assert guage(1) == "E"


def test_guage_f():
    assert guage(99) == "F"
    assert guage(100) == "F"


def test_guage():
    assert guage(50) == "50%"
    assert guage(35) == "35%"
