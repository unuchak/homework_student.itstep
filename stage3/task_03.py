# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 3) Дано натуральное число, определите число десятков в нем (предпоследнюю
# цифру числа). Если предпоследней цифры нет, то можно считать, что число
# десятков равно нулю.

number = int(input("Input a number: "))
if number <= 9:
    print("ERROR")
    exit()

digit = number // 10 % 10

msg = f"""Number of tens: {digit}
of number: {number}"""

print(msg)
