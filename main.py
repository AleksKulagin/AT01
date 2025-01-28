def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def mulitiply(a, b):
    return a * b


def check(number):
    return number % 2 == 0


def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b


def divide_new(a, b):
    """
    Функция для вычисления целого частного и остатка от деления.

    :param a: Делимое (int или float)
    :param b: Делитель (int или float)
    :return: Кортеж (целая часть, остаток)
    :raise ValueError: Если делитель равен нулю
    """
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    quotient = a // b  # Целая часть от деления
    remainder = a % b  # Остаток от деления
    return quotient, remainder
