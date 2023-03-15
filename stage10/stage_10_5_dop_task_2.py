"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
2) Various number digits [различные цифры числа]. Разработайте программу, ко-
торая проверяет, что все цифры заданного натурального числа различны.
"""


def check_unique_digits(num):
    digits = []
    is_unique_digits = True
    while num > 0:
        num, digit = divmod(num, 10)
        if digit in digits:
            is_unique_digits = False
            break
        digits.append(digit)
    return is_unique_digits


def main():
    number = int(input("Input number: "))
    is_unique_digits = check_unique_digits(number)
    msg = build_msg(is_unique_digits)

    print(msg)


def build_msg(is_unique_digits):
    answer = "YES" if is_unique_digits else "NO"
    msg = f"""is unique digits - {answer}"""
    return msg


def test_1_1234567():
    is_unique_digits = check_unique_digits(1234567)
    return is_unique_digits


def test_2_122222():
    is_unique_digits = check_unique_digits(122222)
    return not is_unique_digits


def test_suite():
    msg = f"""
    test_1_1234567 = {test_1_1234567()}
    test_2_122222 = {test_2_122222()}
    """
    print(msg)


test_suite()
main()
