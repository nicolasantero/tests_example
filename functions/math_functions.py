def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def factorial(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    elif n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)