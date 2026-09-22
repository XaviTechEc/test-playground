import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot make a division by zero")
    return a / b


def power(a, b):
    return a**b


def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a**0.5


def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a % b


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def atan(x):
    return math.atan(x)
