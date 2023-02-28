"""
2) Даны следующие арифметические действия: сложение, вычитание, умноже-
ние, деление и остаток от деления. Напишите программу, которая от пользо-
вателя принимает операцию и два вещественных числа, а затем выполняет
указанное действие над этими числами и выводит результат. Если значение
чисел не удовлетворяет указанной операции (к примеру, деление на ноль), то
программа должна вывести соответствующее сообщение.
"""


def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            exit("Error: division by zero")
        else:
            result = num1 / num2
    elif operator == "%":
        if num2 == 0:
            exit("Error: division by zero")
        else:
            result = num1 % num2
    else:
        exit("Error: invalid operator")
    return result


def main():
    operator = input("Enter operator (+, -, *, /, %): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, num2, operator)

    print(f"Result: {result}")


def test_1_5_plus_5():
    operator = "+"
    num1 = float("5")
    num2 = float("5")
    result = calculate(num1, num2, operator)
    return result == 10


def test_2_5_minus_5():
    operator = "-"
    num1 = float("5")
    num2 = float("5")
    result = calculate(num1, num2, operator)
    return result == 0


def test_3_5_division_5():
    operator = "/"
    num1 = float("5")
    num2 = float("5")
    result = calculate(num1, num2, operator)
    return result == 1


def test_4_5_multiply_5():
    operator = "*"
    num1 = float("5")
    num2 = float("5")
    result = calculate(num1, num2, operator)
    return result == 25


def test_5_5_ost_5():
    operator = "%"
    num1 = float("5")
    num2 = float("5")
    result = calculate(num1, num2, operator)
    return result == 0


def test_suite():
    msg = f"test_1_5_plus_5 = {test_1_5_plus_5()}"
    msg += f"\ntest_2_5_minus_5 = {test_2_5_minus_5()}"
    msg += f"\ntest_3_5_division_5 = {test_3_5_division_5()}"
    msg += f"\ntest_4_5_multiply_5 = {test_4_5_multiply_5()}"
    msg += f"\ntest_5_5_ost_5 = {test_5_5_ost_5()}"

    print(msg)


test_suite()
main()
