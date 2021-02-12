import calculator

def test_add_takes_a_string_as_input():
    calculator.add('')

def test_add_when_given_an_empty_string_returns_0():
    assert calculator.add('') == 0