# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 1) Дано натуральное число, выведите его последнюю цифру. Натуральные числа
# – это числа, которые используются при счёте (1, 2, 3, ...).

number = int(input("Input a number: "))
if number <= 0:
    print("ERROR")
    exit()

last_digit = number % 10

msg = f"""The last digit: {last_digit}
of number: {number}"""

print(msg)
