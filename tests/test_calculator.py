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