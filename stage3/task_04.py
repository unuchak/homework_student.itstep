"""
Version 1.0
Author: marina.unuchak
Date: 31.01.2023
4) Дано натуральное пятизначное число. Найдите сумму его цифр.
"""

number = int(input("Input a number: "))
if number < 10000 or number > 100000:
    print("Error, number should be 5-digit")
    exit()

temp = number
summa = 0

while temp > 0:
    temp, digit = divmod(temp, 10)
    summa += digit

msg = f"""Sum of a five-digit number: {summa}
of number: {number}"""

print(msg)
