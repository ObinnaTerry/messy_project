from src.utils import math_operations


def test_add():
    assert math_operations.add(2, 3) == 5

def test_sub():
    assert math_operations.subTract(5, 3) == 2
