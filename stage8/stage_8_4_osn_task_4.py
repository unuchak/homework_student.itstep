"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
4) Beautiful Number [красивое число]. Назовем число красивым, если оно явля-
ется четырехзначным и делится нацело на 9 или на 19. Необходимо написать
программу, определяющую, является ли введённое число красивым. Про-
грамма должна вывести «YES», если число является красивым, или «NO» в
противном случае.
"""


def is_beautiful_number(number):
    if not 1000 <= number <= 9999:
        is_beautiful = False
    else:
        is_beautiful = number % 9 == 0 or number % 19 == 0
    return is_beautiful


def boolean_to_answer(is_beautiful):
    if is_beautiful:
        msg = "YES"
    else:
        msg = "NO"
    return msg


def main():
    number = int(input("Input four-digit number: "))

    is_beautiful = is_beautiful_number(number)
    answer = boolean_to_answer(is_beautiful)

    msg = f"Does the following number beautiful - {answer}"

    print(msg)


def test_1_2280():
    number = 2280
    is_beautiful = is_beautiful_number(number)
    return is_beautiful


def test_2_1710():
    number = 1710
    is_beautiful = is_beautiful_number(number)
    return is_beautiful


def test_3_YES():
    number = True
    answer = boolean_to_answer(number)
    return answer == "YES"


def test_4_NO():
    number = False
    answer = boolean_to_answer(number)
    return answer == "NO"


def test_suite():
    msg = f"""test_1_2280 = {test_1_2280()}
test_2_1710 = {test_2_1710()}
test_3_YES = {test_3_YES()}
test_4_NO = {test_4_NO()}
"""
    print(msg)


test_suite()
main()
