"""
Version 1.0
Author: marina.unuchak
Date: 1.01.2023
1) На вход даётся натуральное число. Выведите следующее за ним чётное число.
Примеры результатов интерактивной программы смотрите ниже на рисунке
(ввод пользователя указан зелёным курсивным шрифтом):
"""

number_1 = int(input("Input a number: "))
number_2 = number_1
number_2 += 1

if number_2 % 2 != 0:
    number_2 += 1

msg = f"""Next even number is: {number_2}
After number: {number_1} 
"""

print(msg)
