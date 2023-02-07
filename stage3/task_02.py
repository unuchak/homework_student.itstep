# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 2) Дано трёхзначное число. Выведите его первую цифру (число сотен).

number = int(input("Input a number: "))
if number < 100 or number > 999:
    print("ERROR")
    exit()

digit = number // 100

msg = f"""The first digit: {digit}
of number: {number}"""

print(msg)
