"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
2) Increasing/decreasing sequence [возрастающая/убывающая последователь-
ность]. Разработайте программу, которая проверяет, что цифры заданного
числа образуют возрастающую (убывающую) последовательность (к примеру,
число 1357 удовлетворяет условию, т.к. его цифры соответствуют следующему
неравенству: 1 < 3 < 5 < 7, т.е. идут в порядке возрастания; число 98765 также
удовлетворяет условию, т.к. его цифры соответствуют следующему неравен-
ству 9 > 8 > 7 > 6 > 5; а вот числа 192837, 777, 19283746 – не удовлетворяют
условию).
"""


def is_sequence(number):
    is_increasing = True
    is_decreasing = True
    while number > 0:
        number, digit = divmod(number, 10)
        next_digit = number % 10
        if next_digit <= digit and next_digit != 0:
            is_increasing = False
        if next_digit >= digit and next_digit != 0:
            is_decreasing = False
    return is_decreasing, is_increasing


def build_msg(is_decreasing, is_increasing):
    if is_increasing:
        msg = "The digits form an increasing sequence."
    elif is_decreasing:
        msg = "The digits form a decreasing sequence."
    else:
        msg = "The digits do not form either an increasing or decreasing sequence."
    return msg


def main():
    number = int(input("Input number: "))

    is_decreasing, is_increasing = is_sequence(number)

    msg = build_msg(is_decreasing, is_increasing)

    print(msg)


def test_1_is_decreasing():
    is_decreasing, is_increasing = is_sequence(1234)
    return is_decreasing and not is_increasing


def test_2_is_decreasing():
    is_decreasing, is_increasing = is_sequence(4321)
    return not is_decreasing and is_increasing


def test_3_not_decreasing_and_not_increasing():
    is_decreasing, is_increasing = is_sequence(5544)
    return not is_decreasing and not is_increasing


def test_suite():
    msg = f"""test_1 is_decreasing = {test_1_is_decreasing()}
test_2 is_increasing =  {test_2_is_decreasing()}
test_3 not decreasing and not increasing =  {test_3_not_decreasing_and_not_increasing()}
"""
    print(msg)


test_suite()
main()
