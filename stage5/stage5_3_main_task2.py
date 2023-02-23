"""
Необходимо написать программу, которая определяет номер (или строковый
эквивалент) дня недели (или день года) для K-го дня любого месяца текущего
года. Дни недели пронумерованы следующим образом: 0 – понедельник, 1 –
вторник, ..., 5 – суббота, 6 – воскресенье, а диапазон дней – 1-365.
"""


def convert_day_of_year__to__day_of_week(day):
    # Sunday first day of the year
    first_day_number_in_year = 6

    day_number_in_year = first_day_number_in_year + day - 1

    day_number = day_number_in_year % 7
    return day_number


def convert_day_of_week_to_text(day_number):
    if day_number == 0:
        return "Monday"
    if day_number == 1:
        return "Tuesday"
    if day_number == 2:
        return "Wednesday"
    if day_number == 3:
        return "Thursday"
    if day_number == 4:
        return "Friday"
    if day_number == 5:
        return "Saturday"
    if day_number == 6:
        return "Sunday"
    return "Error"


def main():
    day = int(input("Enter a day in the range 1-365: "))
    if not (1 <= day <= 365):
        exit("Error, enter a day in the range 1-365")

    day_of_week = convert_day_of_year__to__day_of_week(day)
    day_of_week_text = convert_day_of_week_to_text(day_of_week)

    msg = f"Result: {day_of_week} - {day_of_week_text}"

    print(msg)


main()
