"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
3) Ration [соотношение]. Необходимо написать программу, которая проверяет,
что для заданного четырехзначного числа выполняется следующее соотноше-
ние: сумма первой и последней цифр равна разности второй и третьей цифр.
"""


def ration(number):
    # 1513
    numbers = []
    while number > 0:
        number, digit = divmod(number, 10)
        numbers.append(digit)

    numbers.reverse()

    if len(numbers) > 4 or len(numbers) < 4:
        result = False
    else:
        result = numbers[0] + numbers[3] == numbers[1] - numbers[2]

    return result


def main():
    number = int(input("Input four-digit number: "))

    is_number_ration = ration(number)

    msg = f"Does the following relation hold - {is_number_ration}"

    print(msg)


def test_1_1513():
    number = 1513
    # 1+3 == 5-1
    is_number_ration = ration(number)
    return is_number_ration


def test_2_1413():
    number = 1413
    is_number_ration = ration(number)
    return not is_number_ration


def test_3_113():
    number = 113
    is_number_ration = ration(number)
    return not is_number_ration


def test_4_11343():
    number = 11343
    is_number_ration = ration(number)
    return not is_number_ration


def test_suite():
    msg = f"""test_1_1513 = {test_1_1513()}
test_2_1413 {test_2_1413()}
test_3_113 {test_3_113()}
test_4_11343 {test_4_11343()}
"""
    print(msg)


test_suite()
main()
