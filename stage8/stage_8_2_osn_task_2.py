"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
2) Quantity [количество]. Необходимо написать программу, которая считывает
четыре числа и подсчитывает количество только положительных (отрицатель-
ных или нулевых) чисел.
"""
AMOUNT_OF_NUMBERS = 4


def count_of_positive_numbers(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1

    return count


def count_of_negative_numbers(numbers):
    count = 0
    for number in numbers:
        if number < 0:
            count += 1

    return count


def count_of_zero(numbers):
    count = 0
    for number in numbers:
        if number == 0:
            count += 1

    return count


def main():
    numbers = []
    size = AMOUNT_OF_NUMBERS
    for _ in range(size):
        number = int(input(" Input number: "))
        numbers.append(number)
    count_of_positive = count_of_positive_numbers(numbers)
    count_of_negative = count_of_negative_numbers(numbers)
    count_of_0 = count_of_zero(numbers)

    msg = f""" Count of positive numbers {count_of_positive}, 
Count of negative numbers  {count_of_negative}
Count of zero {count_of_0}"""

    print(msg)


def test():
    numbers = [7, 9, -4, 0]
    count_of_positive = count_of_positive_numbers(numbers)
    count_of_negative = count_of_negative_numbers(numbers)
    count_of_0 = count_of_zero(numbers)
    return count_of_positive == 2 and count_of_negative == 1 and count_of_0 == 1


def test_suite():
    msg = f" test = {test()}"
    print(msg)


test_suite()

main()
