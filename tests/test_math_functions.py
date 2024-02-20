from functions.math_functions import add_numbers, multiply_numbers, factorial

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-2, 3) == 1
    assert add_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(0, 5) == 0

def test_factorial():
    # Test factorial of 0
    assert factorial(0) == 1

    # Test factorial of 1
    assert factorial(1) == 1

    # Test factorial of a positive number
    assert factorial(5) == 120

    # Test factorial of a negative number
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "n must be a non-negative integer"

    # Test factorial of a non-integer
    try:
        factorial(2.5)
    except ValueError as e:
        assert str(e) == "n must be an integer"