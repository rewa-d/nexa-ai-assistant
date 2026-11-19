
from src.tools.calculator import calculate


def test_calculator():
    assert calculate(10, 5, "add") == 15
    assert calculate(10, 5, "subtract") == 5
    assert calculate(10, 5, "multiply") == 50
    assert calculate(10, 5, "divide") == 2

    print("All calculator tests passed!")


def test_division_by_zero():
    try:
        calculate(10, 0, "divide")
        raise AssertionError("Expected ValueError")
    except ValueError:
        print("Division by zero handled correctly!")


def test_invalid_operation():
    try:
        calculate(10, 5, "power")
        raise AssertionError("Expected ValueError")
    except ValueError:
        print("Invalid operation handled correctly!")


if __name__ == "__main__":
    test_calculator()
    test_division_by_zero()
    test_invalid_operation()
