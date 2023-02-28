"""
4) Дано натуральное число N (0 <= N <= 999). Напишите интерактивную про-
грамму, которая организует диалог с пользователем и записывает число ан-
глийскими (русскими) словами. Ниже приведён рекомендуемый вид экрана во
время работы программы. Ввод пользователя выделен полужирным шрифтом.
Если N не лежит в указанном диапазоне то вывести соответствующее сообщение
"""


def num_to_words(num):
    units_list = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens_list = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                 "девяносто"]
    teens_list = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                  "семнадцать", "восемнадцать", "девятнадцать"]
    hundred_list = ["", "сто", "двести", "триста", "четыреста"]

    if num < 10:
        return units_list[num]

    elif num < 20:
        return teens_list[num - 10]

    elif num < 100:
        tens_word = tens_list[num // 10]
        units_word = num_to_words(num % 10) if num % 10 > 0 else ""
        return f"{tens_word} {units_word}"

    else:
        hundred = num // 100
        if hundred < 5:
            hundred_word = hundred_list[hundred]
        else:
            hundred_word = f"{units_list[hundred]}сот"
        tens_and_units_word = num_to_words(num % 100) if num % 100 > 0 else ""
        return f"{hundred_word} {tens_and_units_word}"


def main():
    num = input("Введите число от 0 до 999: ")

    if not num.isdigit():
        exit("Ошибка: введено не число.")

    num = int(num)

    if num < 0 or num > 999:
        exit("Ошибка: число должно быть от 0 до 999.")

    words = num_to_words(num)

    print(words)


def test_1_19():
    num = int("19")
    words = num_to_words(num)
    return words == "девятнадцать"


def test_2_6():
    num = int("6")
    words = num_to_words(num)
    return words == "шесть"


def test_3_196():
    num = int("196")
    words = num_to_words(num)
    return words == "сто девяносто шесть"


def test_suite():
    msg = f"test_1_19 = {test_1_19()}"
    msg += f"\ntest_2_6 = {test_2_6()}"
    msg += f"\ntest_3_196 = {test_3_196()}"

    print(msg)


test_suite()
main()
