"""
Version 1.0
Author: marina.unuchak
Date: 5.01.2023
4) Длина Минской кольцевой автомобильной дороги – 56 километров. Байкер
стартует с нулевого километра МКАД и едет со скоростью V километров в час.
На какой отметке он остановится через T часов? Программа получает на вход
целые числа V и T. Если V > 0, то байкер движется в положительном направ-
лении по МКАД, если же значение V < 0, то в отрицательном. 0 ≤ T ≤ 1000, -
1 ≤ V ≤ 100.
"""

speed_km_h = int(input(":Input speed kilometers per hour: "))
time_stop_h = int(input("Input time to stop: "))
if 0 <= time_stop_h <= 1000 and 1 <= speed_km_h <= 100:
    # length_of_circle- Длина Минской кольцевой автомобильной дороги – 56 километров
    length_of_circle = 56
    # total_length - Расстояние которое он проехал
    total_length = speed_km_h * time_stop_h
    # point_of_circle - Отметка на какой он остановится через T часов
    point_of_circle = total_length % length_of_circle

    msg = f"""A mark on which Biker will stop after {time_stop_h} hours: 
    {point_of_circle} kilometer"""

    print(msg)

else:
    error = "Error, should be: 0 ≤ time_stop_h ≤ 1000, 1 ≤ speed_km_h ≤ 100"
    print(error)
    exit()
