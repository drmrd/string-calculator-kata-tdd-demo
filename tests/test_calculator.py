import calculator


def test_add_when_given_an_empty_string_returns_0():
    assert calculator.add('') == 0