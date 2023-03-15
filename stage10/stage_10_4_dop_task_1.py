"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
1) Reversу number digits [реверсирование цифр числа]. Разработайте программу,
которая переворачивает заданное целое число. При этом, если число отрица-
тельное, то в результате реверсирования также должно получиться отрица-
тельное число. Последние нули числа должны оставаться на своих местах при
реверсировании. К примеру, число 1234567 реверсируется в следующее
число 7654321, число -789 – в число -987, а число 125000 – в число 521000.
"""


def reverse_number(num):
    sign = 1 if num >= 0 else -1
    num = abs(num)
    reversed_num = 0
    while num > 0:
        num, digit = divmod(num, 10)
        reversed_num = reversed_num * 10 + digit
    return sign * reversed_num


def main():
    number = int(input("Input number: "))
    number_reversed = reverse_number(number)
    msg = build_msg(number_reversed)

    print(msg)


def build_msg(number_reversed):
    msg = f"""Number reversed is {number_reversed}"""
    return msg


def test_1_1234567():
    number_reversed = reverse_number(1234567)
    return number_reversed == 7654321


def test_2__1234567():
    number_reversed = reverse_number(-1234567)
    return number_reversed == -7654321


def test_suite():
    msg = f"""
    test_1_1234567 = {test_1_1234567()}
    test_2__1234567 = {test_2__1234567()}
    """
    print(msg)


test_suite()
main()
