"""
1) Дано целое число в диапазоне от 1 до 120, определяющее возраст (в годах).
Написать программу, которая выводит строку-описание указанного возраста,
обеспечив правильное согласование числа со словом «год», например: 20 –
«двадцать лет», 32 – «тридцать два года», 41 – «сорок один год» и т.д.
"""

PLURAL_FEW = 1
PLURAL_MANY = 2
PLURAL_OTHER = 3


def get_year_suffix(age):
    plural = get_number_plural(age)
    suffix = get_year_suffix_by_plural(plural)
    return suffix


def get_number_plural(number):
    last_digit = number % 10

    if last_digit == 1:
        return PLURAL_FEW
    elif last_digit in [2, 3, 4]:
        return PLURAL_MANY
    else:
        return PLURAL_OTHER


def get_year_suffix_by_plural(plural):
    if plural == PLURAL_FEW:
        return "год"
    elif plural == PLURAL_MANY:
        return "года"
    else:
        return "лет"


def main():
    age = int(input("Enter an age from 1 to 120 years old: "))

    suffix = get_year_suffix(age)

    print(f"{age} {suffix}")


def test_1_get_number_plural_1():
    number = 1
    plural = get_number_plural(number)
    return plural == PLURAL_FEW


def test_2_get_number_plural_2():
    number = 2
    plural = get_number_plural(number)
    return plural == PLURAL_MANY


def test_3_get_number_plural_5():
    number = 2
    plural = get_number_plural(number)
    return plural == PLURAL_OTHER


def test_4_get_year_suffix_5():
    age = 5
    suffix = get_year_suffix(age)
    return suffix == "лет"


def test_suite():
    msg = f"test_1_get_number_plural_1 = {test_1_get_number_plural_1()}"
    msg += f"\ntest_2_get_number_plural_2 = {test_2_get_number_plural_2()}"
    msg += f"\ntest_3_get_number_plural_5 = {test_3_get_number_plural_5()}"
    msg += f"\ntest_4_get_year_suffix_5 = {test_4_get_year_suffix_5()}"

    print(msg)


test_suite()
main()
