"""
5) Даны два неотрицательных целых числа: годи и месяц (целое число в диапа-
зоне то 1 до 12, где 1 -January, 2 – February, 3 – March и т. д.). Напишите про-
грамму, которая определяет количество дней в этом месяце для невисокос-
ного года. Если числа не лежат в указанном диапазоне то вывести соответству-
ющее сообщение.
"""


def determinate_name_of_month(month):
    if month == 1:
        month_name = "January"
    elif month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"
    elif month == 4:
        month_name = "April"
    elif month == 5:
        month_name = "May"
    elif month == 6:
        month_name = "June "
    elif month == 7:
        month_name = "July"
    elif month == 8:
        month_name = "August"
    elif month == 9:
        month_name = "September"
    elif month == 10:
        month_name = "October"
    elif month == 11:
        month_name = "November"
    elif month == 12:
        month_name = "December"
    else:
        month_name = "Error"

    return month_name


def calc_days_of_month(month):
    if any([
        month == 1,
        month == 3,
        month == 5,
        month == 7,
        month == 8,
        month == 10,
        month == 12
    ]):
        return 31
    elif any([
        month == 4,
        month == 6,
        month == 9,
        month == 11
    ]):
        return 31
    elif month == 2:
        return 28
    else:
        exit(f"Error with month = {month}")


def full_text_year_and_days_of_month(year, month):
    days_a_month = str(calc_days_of_month(month))
    month_of_the_year = determinate_name_of_month(month)

    return f"{year} year, {month_of_the_year}: {days_a_month}"


def main():
    year, month = map(int, input("Input a year, month: ").split(","))

    if not (year > 0):
        exit("Error, should be year > 0")

    if not (1 <= month <= 12):
        exit("Error, should be 1 <= month <= 12")

    full_text = full_text_year_and_days_of_month(year, month)

    msg = f"Result: {full_text} days"

    print(msg)


def test_1_month_1():
    month = 1
    name_of_month = determinate_name_of_month(month)
    return name_of_month == "January"


def test_2_month_2():
    month = 2
    name_of_month = determinate_name_of_month(month)
    return name_of_month == "February"


def test_3_month_3():
    month = 3
    name_of_month = determinate_name_of_month(month)
    return name_of_month == "March"


def test_4_month_13():
    month = 13
    name_of_month = determinate_name_of_month(month)
    return name_of_month == "Error"


def test_suite():
    msg = f"test_1_month_1 = {test_1_month_1()}"
    msg += f"\ntest_2_month_2 = {test_2_month_2()}"
    msg += f"\ntest_3_month_3 = {test_3_month_3()}"
    msg += f"\ntest_4_month_13 = {test_4_month_13()}"

    print(msg)


test_suite()
main()
