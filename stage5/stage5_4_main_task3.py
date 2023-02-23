"""
Дано четырехзначное число. Определите, является ли его десятичная запись
симметричной. Число может иметь меньше четырех знаков, тогда нужно счи-
тать, что его десятичная запись дополняется слева незначащими нулями. При-
меры результатов интерактивной программы смотрите ниже на рисунке (ввод
пользователя указан зелёным курсивным шрифтом):
"""


def is_equal(number):
    number_1, number_2 = divmod(number, 100)
    number_1_1, number_1_2 = divmod(number_1, 10)
    new_number_1 = number_1_2 * 10 + number_1_1

    if new_number_1 == number_2:
        msg = "Yes"
    else:
        msg = "No"
    return msg


def main():
    number = int(input("Введите 4x-значное число: "))
    if not 100 <= number <= 9999:
        exit("Error, should me 100 <= number <= 9999")

    msg = is_equal(number)

    print(msg)


main()
