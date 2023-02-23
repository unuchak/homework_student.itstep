"""
Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день
на A метров, а за ночь спускаясь на B метров. На какой день улитка доползёт
до вершины шеста? Программа получает на вход целые неотрицательные
числа H, A, B, причем H > B и A > B. Примеры результатов интерактивной про-
граммы смотрите ниже на рисунке (ввод пользователя указан зелёным курсив-
ным шрифтом):
"""


def calc_day(h, a, b):
    if h <= b:
        exit("Error, should be H > B")
    if a <= b:
        exit("Error, should be A > B")

    day = 0
    while h > 0:
        day += 1
        h -= a
        if h < 0:
            break
        h += b

    return day


def main():
    h = int(input("Input H: "))
    a = int(input("Input A: "))
    b = int(input("Input B: "))

    day = calc_day(h, a, b)
    msg = f"After {day} days."

    print(msg)


main()
