"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
1) Amount [сумма]. Необходимо написать программу, которая считывает четыре
числа и подсчитывает сумму только положительных (отрицательных) чисел.
"""
AMOUNT_OF_NUMBERS = 4


def sum_of_positive_numbers(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number

    return summa


def sum_of_negative_numbers(numbers):
    summa = 0
    for number in numbers:
        if number < 0:
            summa += number

    return summa


def main():
    numbers = []
    size = AMOUNT_OF_NUMBERS
    for _ in range(size):
        number = int(input(" Input number: "))
        numbers.append(number)
    sum_of_positive = sum_of_positive_numbers(numbers)
    sum_of_negative = sum_of_negative_numbers(numbers)

    msg = f""" Sum of positive numbers {sum_of_positive}, 
Sum of negative numbers  {sum_of_negative}"""

    print(msg)


def test():
    numbers = [7, 9, -4, 0]
    sum_of_positive = sum_of_positive_numbers(numbers)
    sum_of_negative = sum_of_negative_numbers(numbers)
    return sum_of_positive == 16 and sum_of_negative == -4


def test_suite():
    msg = f" test = {test()}"
    print(msg)


test_suite()

main()
