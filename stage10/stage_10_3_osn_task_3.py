"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
3) The palindrome [число-палиндромом]. Разработайте программу, которая про-
веряет, что заданное натуральное число читается одинаково слева направо и
справа налево (т.е. является палиндромом). К примеру, числа 1235321, 112211,
7 и 1221 – удовлетворяют условию, а числа 12345321, 1000 и 12 – нет.
"""


def is_number_palindrome(num):
    digits = list(str(num))
    is_palindrome = True
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i - 1]:
            is_palindrome = False
            break
    return is_palindrome


def main():
    num = input("Enter a number: ")
    is_palindrome = is_number_palindrome(num)
    msg = build_msg(is_palindrome)

    print(msg)


def build_msg(is_palindrome):
    if is_palindrome:
        msg = "The number is palindrome."
    else:
        msg = "The number is not palindrome"
    return msg


def test_1_1235321():
    is_palindrome = is_number_palindrome(1235321)
    return is_palindrome


def test_2_112211():
    is_palindrome = is_number_palindrome(112211)
    return is_palindrome


def test_3_7():
    is_palindrome = is_number_palindrome(7)
    return is_palindrome


def test_4_1221():
    is_palindrome = is_number_palindrome(1221)
    return is_palindrome


def test_suite():
    msg = f"""
    test_1_1235321 = {test_1_1235321()}
    test_2_112211 =  {test_2_112211()}
    test_3_7 =  {test_3_7()}
    test_4_1221 =  {test_4_1221()}
    """
    print(msg)


test_suite()
main()
