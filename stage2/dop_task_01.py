# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 1)В некоторой школе решили набрать три новых математических класса и обо-
# рудовать кабинеты для них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в каждом из трех классов. Вы-
# ведите наименьшее число парт, которое нужно приобрести для них. Каждый
# класс сидит в своем кабинете.

class_a = int(input("Input number of students (a) class: "))
class_b = int(input("Input number of students (b) class: "))
class_c = int(input("Input number of students (c) class: "))

min_number_of_desks = min(class_a, class_b, class_c)
result, rest = divmod(min_number_of_desks, 2)
if rest > 0:
    result += 1

msg = f"""Min_number_of_desks: {result}"""

print(msg)
