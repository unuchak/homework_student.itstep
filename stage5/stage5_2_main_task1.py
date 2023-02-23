"""
1) Необходимо написать программу определения соответствующего столетия для
заданного года (целое положительное число), учитывая, что, к примеру, нача-
лом XX столетия был 1901 год
"""

import math


def convert_year_to_century_roman(year):
    century = math.ceil(year / 100)
    thousands, hundreds = divmod(century, 10)

    thousands_roman = thousands * "X"
    if hundreds == 1:
        hundreds_roman = "I"
    elif hundreds == 2:
        hundreds_roman = "II"
    elif hundreds == 3:
        hundreds_roman = "III"
    elif hundreds == 4:
        hundreds_roman = "IV"
    elif hundreds == 5:
        hundreds_roman = "V"
    elif hundreds == 6:
        hundreds_roman = "VI"
    elif hundreds == 7:
        hundreds_roman = "VII"
    elif hundreds == 8:
        hundreds_roman = "VIII"
    elif hundreds == 9:
        hundreds_roman = "IX"
    else:
        hundreds_roman = ""

    century_roman = thousands_roman + hundreds_roman
    return century_roman


def main():
    year = int(input("Input year: "))

    result = convert_year_to_century_roman(year)

    msg = f"Century: {result}"

    print(msg)


main()
