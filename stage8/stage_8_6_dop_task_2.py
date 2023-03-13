"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
4) Extreme Number 2 [экстремальное число]. Необходимо написать оптималь-
ную программу, которая считывает четыре числа и определяет максимальное
(минимальное) из них.
"""


def get_extreme_number(number1, number2, number3, number4):
    max_num = max(number1, number2, number3, number4)
    min_num = min(number1, number2, number3, number4)
    return max_num, min_num


def build_message(max_num, min_num):
    return f"max number: {max_num}\nmin number: {min_num}"


def main():
    number1, number2, number3, number4 = map(int, input("Enter four numbers:").split())

    max_num, min_num = get_extreme_number(number1, number2, number3, number4)
    msg = build_message(max_num, min_num)

    print(msg)


def test_1__1_2_3_4():
    max_num, min_num = get_extreme_number(1, 2, 3, 4)
    return max_num == 4 and min_num == 1


def test_2__2_4_6_8():
    max_num, min_num = get_extreme_number(2, 4, 6, 8)
    return max_num == 8 and min_num == 2


def test_3__1_2_3_5():
    max_num, min_num = get_extreme_number(1, 2, 3, 5)
    return max_num == 5 and min_num == 1


def test_suite():
    msg = f"""test_1__1_2_3_4 = {test_1__1_2_3_4()}
test_2__2_4_6_8 = {test_2__2_4_6_8()}
test_3__1_2_3_5 = {test_3__1_2_3_5()}
"""
    print(msg)


test_suite()
main()
