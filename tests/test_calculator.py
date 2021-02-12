import pytest

import calculator


def test_add_when_given_an_empty_string_returns_0():
    assert calculator.add('') == 0


def test_add_when_given_1_as_a_string_returns_1():
    assert calculator.add('1') == 1


def test_add_when_given_2_as_a_string_returns_2():
    assert calculator.add('2') == 2


def test_add_when_given_negative_integer_returns_that_number():
    assert calculator.add('-3') == -3


def test_add_when_given_1_and_2_by_a_comma_returns_their_sum():
    assert calculator.add('1,2') == 3


def test_add_when_given_1_and_3_by_a_comma_returns_their_sum():
    assert calculator.add('1,3') == 4


def test_that_add_fails_when_given_more_than_two_integers_in_its_input_string():
    with pytest.raises(ValueError):
        assert calculator.add('2,3,5')