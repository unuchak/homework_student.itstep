# Version 1.0
# Author: marina.unuchak
# Date: 5.01.2023
# Разработать исследовательскую программу, которая тестировала бы все воз-
# можные арифметические операции над «простыми» (примитивными) типами
# данных в Python. К простым стандартным типам данных можно отнести целые
# числа (int), числа с плавающей запятой (float), булевский тип (bool) и строки
# (str). Сделать соответствующий анализ результатов и выводы.

v = int(input(":Input speed kilometers per hour: "))
t = int(input("Input time to stop: "))
if 0 <= t <= 1000 and 1 <= v <= 100:
    # l- Длина Минской кольцевой автомобильной дороги – 56 километров
    l = 56
    # s - Расстояние которое он проехал
    s = v * t
    # p - Отметка на какой он остановится через T часов
    p = s % l

    msg = f"""A mark on which Biker will stop after {t} hours: 
    {p} kilometer"""

    print(msg)

else:
    error = "Error, values should be: 0 ≤ T ≤ 1000, 1 ≤ V ≤ 100"
    print(error)
    exit()
