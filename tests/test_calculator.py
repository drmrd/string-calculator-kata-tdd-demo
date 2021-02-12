from pytest import fixture

import calculator

def test_add_takes_a_string_as_input():
    calculator.add('')