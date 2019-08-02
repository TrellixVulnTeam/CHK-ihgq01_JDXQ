import pytest
from solutions.CHK import checkout_solution


def test_checkout_solution_illegal():
    result = checkout_solution.checkout('AHDFE')
    assert result == -1


def test_checkout_solution():
    result = checkout_solution.checkout('AAAC')
    assert result == 150


def test_checkout_solution_2():
    result = checkout_solution.checkout('CBABA')
    assert result == 160