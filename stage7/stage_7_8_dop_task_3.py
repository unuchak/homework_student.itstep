"""
3) Даны два целых числа, соответствующие дню и месяцу и определяющие пра-
вильную дату. Написать программу, которая выводит знак Зодиака, соответ-
ствующий этой дате: «Водолей» (20.1-18.2), «Рыбы» (19.2-20.3), «Овен» (21.3-
19.4), «Телец» (20.4-20.5), «Близнецы» (21.5-21.6), «Рак» (22.6-22.7), « Лев» (23.7-22.8), «Дева» (23.8-22.9),
«Весы» (23.9-22.10), «Скорпион» (23.10-22.11), «Стрелец» (23.11-21.12) и «Козерог» (22.12-19.1)
"""


def get_constellation_by_date(day, month):
    if not 1 <= day <= 31:
        exit("day should be 1 <= day <= 31")
    if not 1 <= month <= 12:
        exit("day should be 1 <= month <= 12")

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Близнецы"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    else:
        return "Козерог"


def main():
    day = int(input("Input day: "))
    month = int(input("Input month: "))
    constellation = get_constellation_by_date(day, month)
    print(constellation)


def test_1_19_12():
    day = int("19")
    month = int("12")
    constellation = get_constellation_by_date(day, month)
    return constellation == "Стрелец"


def test_2_9_6():
    day = int("9")
    month = int("6")
    constellation = get_constellation_by_date(day, month)
    return constellation == "Близнецы"


def test_suite():
    msg = f"test_1_19_12 = {test_1_19_12()}"
    msg += f"\ntest_2_9_6 = {test_2_9_6()}"

    print(msg)


test_suite()
main()
