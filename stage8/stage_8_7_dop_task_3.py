"""
The program prints my favotite phrase

Version 1.0
Author: marina.unuchak
Date: 13.02.2023
"""
"""
4) Century [столетие]. Необходимо написать программу определения соответ-
ствующего столетия для заданного года (целое положительное или отрица-
тельное число), учитывая, что, к примеру, началом XX столетия нашей эры был
1901 год. Программа должна определять столетия не только нашей эры (AD –
anno Domini), но и до нашей эры, до рождества Христова (BC – before Christ).
"""


def get_century_period(year):
    if year < 0:
        period = "BC"
    else:
        period = "AD"

    return period


def get_century(year):
    if year < 0:
        year = abs(year)

    if year % 100 == 0:
        century = year // 100
    else:
        century = year // 100 + 1

    return century


def build_message(century, period):
    return f"{century}th century {period}"


def main():
    year = int(input("Enter a year: "))

    century = get_century(year)
    period = get_century_period(year)
    msg = build_message(century, period)

    print(msg)


def test_1__2023_century():
    century = get_century(2023)
    return century == 21


def test_2__2023_period():
    period = get_century_period(2023)
    return period == "AD"


def test_suite():
    msg = f"""test_1__2023_century = {test_1__2023_century()}
test_2__2023_period = {test_2__2023_period()}
"""
    print(msg)


test_suite()
main()
