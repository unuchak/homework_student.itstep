"""
Необходимо написать программу, которая определяет номер (или строковый
эквивалент) дня недели (или день года) для K-го дня любого месяца текущего
года. Дни недели пронумерованы следующим образом: 0 – понедельник, 1 –
вторник, ..., 5 – суббота, 6 – воскресенье, а диапазон дней – 1-365.
"""


def convert_day_of_year__to__day_of_week(day):
    # первый день в текущем году воскресенье
    first_day_number_in_year = 6

    day_number_in_year = first_day_number_in_year + day - 1

    day_number = day_number_in_year % 7
    return day_number


def convert_day_of_week_to_text(day_number):
    if day_number == 0:
        return "понедельник"
    if day_number == 1:
        return "вторник"
    if day_number == 2:
        return "среда"
    if day_number == 3:
        return "четверг"
    if day_number == 4:
        return "пятница"
    if day_number == 5:
        return "суббота"
    if day_number == 6:
        return "воскресенье"
    return "Error"


def main():
    day = int(input("Введите день в диапазоне 1-365: "))
    if not (1 <= day <= 365):
        exit("Error, введите день в диапазоне 1-365")

    day_of_week = convert_day_of_year__to__day_of_week(day)
    day_of_week_text = convert_day_of_week_to_text(day_of_week)

    msg = f"Result: {day_of_week} - {day_of_week_text}"

    print(msg)


main()
