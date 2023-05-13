"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
3) The largest series of identical digits of a number [наибольшая серия одинако-
вых цифр числа]. Необходимо написать программу, которая определяет
наибольшее число подряд идущих цифр заданного пользователем числа. Если
не нашлось ни одной пары, тройки и т.д. цифр числа, равных друг другу, то
программа должна вывести число 1
"""


def get_digits_of_number(num):
    digits = []

    while num > 0:
        num, digit = divmod(num, 10)
        digits.append(digit)

    return digits


def largest_series(num):
    digits = get_digits_of_number(num)

    max_count = 1
    count = 1
    for i in range(1, len(digits)):
        if digits[i] == digits[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)
    return max_count


def main():
    num = input("Enter a number: ")
    series = largest_series(num)
    msg = build_msg(series)

    print(msg)


def build_msg(series):
    return f"The number largest series is {series}"


def test_1_1234567():
    series = largest_series(1234567)
    return series == 1


def test_2_1111():
    series = largest_series(1111)
    return series == 4


def test_3_123444321():
    series = largest_series(123444321)
    return series == 3


def test_suite():
    msg = f"""
    test_1_1234567 = {test_1_1234567()}
    test_2_1111 = {test_2_1111()}
    test_3_123444321 =  {test_3_123444321()}
    """
    print(msg)


test_suite()
main()
