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


def is_arithmetic_progression(number1, number2, number3, number4):
    return number4 - number3 == number3 - number2 == number2 - number1


def boolean_to_answer(is_right):
    if is_right:
        msg = "YES"
    else:
        msg = "NO"
    return msg


def build_message(is_right):
    answer = boolean_to_answer(is_right)
    return f"Are the numbers consecutive components of an arithmetic progression? - {answer}"


def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))

    is_right = is_arithmetic_progression(number1, number2, number3, number4)
    msg = build_message(is_right)

    print(msg)


def test_1__1_2_3_4():
    is_right = is_arithmetic_progression(1, 2, 3, 4)
    return is_right


def test_2__2_4_6_8():
    is_right = is_arithmetic_progression(2, 4, 6, 8)
    return is_right


def test_3__1_2_3_5():
    is_right = is_arithmetic_progression(1, 2, 3, 5)
    return not is_right


def test_4_YES():
    number = True
    answer = boolean_to_answer(number)
    return answer == "YES"


def test_5_NO():
    number = False
    answer = boolean_to_answer(number)
    return answer == "NO"


def test_suite():
    msg = f"""test_1__1_2_3_4 = {test_1__1_2_3_4()}
test_2__2_4_6_8 = {test_2__2_4_6_8()}
test_3__1_2_3_5 = {test_3__1_2_3_5()}
test_4_YES = {test_4_YES()}
test_5_NO = {test_5_NO()}
"""
    print(msg)


test_suite()
main()
