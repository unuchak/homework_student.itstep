"""
2) Дано целое число в диапазоне от 1 до 7, соответствующее дню недели (1 -
Monday, 2 – Thursday, 3 – Wednesday и т. д.). Напишите программу, которая
согласно номеру выводит название соответствующего дня недели. Если целое
число не лежит в указанном диапазоне то вывести соответствующее сообще-
ние.
"""


def determine_the_day_of_the_week(day_number):
    if day_number == 1:
        return "Monday"
    if day_number == 2:
        return "Tuesday"
    if day_number == 3:
        return "Wednesday"
    if day_number == 4:
        return "Thursday"
    if day_number == 5:
        return "Friday"
    if day_number == 6:
        return "Saturday"
    if day_number == 7:
        return "Sunday"
    return "Error"


def main():
    day = int(input("Input day of the week number: "))

    day_of_week = determine_the_day_of_the_week(day)

    msg = f"Result: {day_of_week} "

    print(msg)


# main()


def test_1_monday():
    day = 1
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "Monday"


def test_2_tuesday():
    day = 2
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "Tuesday"


def test_3_wednesday():
    day = 3
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "Wednesday"


def test_4_thursday():
    day = 4
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "Thursday"


def test_5_friday():
    day = 5
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "Friday"


def test_6_saturday():
    day = 6
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "saturday"


def test_7_sunday():
    day = 7
    day_of_week = determine_the_day_of_the_week(day)
    return day_of_week == "sunday"


def test_suite():
    msg = f"test_1_monday - {test_1_monday()}"
    msg += f"\ntest_2_tuesday - {test_2_tuesday()}"
    msg += f"\ntest_3_wednesday - {test_3_wednesday()}"
    msg += f"\ntest_4_thursday - {test_4_thursday()}"
    msg += f"\ntest_5_friday - {test_5_friday()}"
    msg += f"\ntest_6_saturday - {test_6_saturday()}"
    msg += f"\ntest_7_sunday - {test_7_sunday()}"

    print(msg)


test_suite()
main()
