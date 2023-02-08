"""
Version 1.0
Author: marina.unuchak
Date: 5.01.2023
Разработать исследовательскую программу, которая тестировала бы все воз-
можные арифметические операции над «простыми» (примитивными) типами
данных в Python. К простым стандартным типам данных можно отнести целые
числа (int), числа с плавающей запятой (float), булевский тип (bool) и строки
(str). Сделать соответствующий анализ результатов и выводы.
"""


def arithmetic_operations(a, b):
    type_of_a = type(a)
    s = f"Result of testing Arithmetic Operations on {type_of_a} data type in Python"
    c = a + b
    s += f"1) addition:\t\t {a} + {b} = {c}\n"
    c = a - b
    s += f"2) subtraction:\t\t {a} - {b} = {c}\n"
    c = b - a
    s += f"3) subtraction:\t\t {b} - {a} = {c}\n"
    c = a * b
    s += f"4) multiplication:\t {a} * {b} = {c}\n"
    c = b / a
    s += f"5) division:\t\t {b} / {a} = {c}\n"
    c = b // a
    s += f"6) floor division:\t {b} // {a} = {c}\n"
    s += f"7) division:\t\t {a} / {b} => ZeroDivisionError: division by zero\n"
    s += f"8) division:\t\t {a} // {b} => ZeroDivisionError: division by zero\n"
    c = b % a
    s += f"9) modulus:\t\t\t {b} % {a} = {c}\n"
    s += f"10) modulus:\t\t {a} % {b} => ZeroDivisionError: division or modulo by zero\n"
    c = a ** b
    s += f"11) exponentiation:\t {a}**{b} = {c}\n"
    c = b ** a
    s += f"12) exponentiation:\t {b}**{a} = {c}"
    print(s)


def arithmetic_operations_str(a: str, b: str):
    print("Result of testing Arithmetic Operations on str data type in Python")
    c = a + b
    s = f"1) addition:\t\t {a} + {b} = {c}\n"
    print(s)


arithmetic_operations(True, False)
arithmetic_operations(1, 2)
arithmetic_operations(1.1, 2.2)
arithmetic_operations_str("1.1", "2.2")
