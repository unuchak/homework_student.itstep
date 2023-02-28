"""
5) Заданы три целых числа, которые задают некоторую дату по Грегорианскому
календарю Определить дату следующего дня. Запрещается использовать типы стандартной биб-
лиотеки языка для работы с датой и временем. Также необходимо учесть то,
что по григорианскому календарю (используется в настоящим момент) висо-
косный год определяется следующим образом:
 годы, кратные 4 – високосные (например, 2008, 2012, 2016);
 годы, кратные 4 и 100 – невисокосные (например, 1700, 1800, 1900);
 годы, кратные 4, 100 и 400 – високосные (например, 1600, 2000, 2400)
"""


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def calculate_next_day(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    if day < days_in_month[month - 1]:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return year, month, day


def main():
    year = int(input("Введите год (yyyy): "))
    month = int(input("Введите месяц (m): "))
    day = int(input("Введите день (d): "))

    next_year, next_month, next_day = calculate_next_day(year, month, day)

    print(f"Следующий день: {next_day}.{next_month}.{next_year}")


def test_1_9_6():
    year = int("1994")
    month = int("6")
    day = int("9")

    next_year, next_month, next_day = calculate_next_day(year, month, day)
    return next_day == 10 and next_month == 6 and next_year == 1994


def test_suite():
    msg = f"test_1_9_6 = {test_1_9_6()}"

    print(msg)


test_suite()
main()
