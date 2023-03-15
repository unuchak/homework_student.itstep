"""
Version 1.0
Author: marina.unuchak
Date: 14.02.2023
"""
"""
1) Bank deposit [банковский вклад]. Начальный вклад в банке равен N руб. При
ежемесячной капитализации через каждый месяц размер вклада увеличива-
ется на P процентов от имеющейся суммы (P может быть как вещественным
числом, так и целым). По данному P определить, через сколько месяцев раз-
мер вклада удвоится, и вывести найденное количество месяцев K (целое
число) и итоговый размер вклада S (вещественное число).

"""


def calc_bank_deposit(initial_deposit, interest_rate):
    amount = initial_deposit
    number_of_months = 0
    while amount < 2 * initial_deposit:
        amount += amount * (interest_rate / 100)
        number_of_months += 1
    return number_of_months, amount


def build_msg(amount, number_of_months):
    msg = f"The deposit amount will double after {number_of_months} months and will be {amount:.2f} rubles."
    return msg


def main():
    initial_deposit = float(input("Enter the initial deposit: "))
    interest_rate = float(input("Enter the interest rate: "))

    number_of_months, amount = calc_bank_deposit(initial_deposit, interest_rate)

    msg = build_msg(amount, number_of_months)

    print(msg)


def test():
    initial_deposit = 10000
    number_of_months, amount = calc_bank_deposit(initial_deposit, 1.5)
    return number_of_months == 47 and amount // initial_deposit == 2


def test_suite():
    msg = f" test = {test()}"
    print(msg)


test_suite()
main()
