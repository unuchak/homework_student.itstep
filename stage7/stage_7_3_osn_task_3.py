"""
3) Напишите программу, которая определяла бы, является ли заданное число N
кратным соответствующему числу M.
"""


def definition_of_multiplicity(number_1, number_2):
    if number_2 > number_1:
        return False

    if number_1 % number_2 == 0:
        msg = True
    else:
        msg = False

    return msg


def main():
    number_n = int(input("Input a number N: "))
    number_m = int(input("Input a number M: "))
    is_multiplicity = definition_of_multiplicity(number_n, number_m)

    msg = f"Result: {is_multiplicity} "

    print(msg)


# main()

def test_1_is_6_multiplicity_3():
    number_n = 6
    number_m = 3
    is_multiplicity = definition_of_multiplicity(number_n, number_m)
    return is_multiplicity


def test_2_is_12_multiplicity_6():
    number_n = 12
    number_m = 6
    is_multiplicity = definition_of_multiplicity(number_n, number_m)
    return is_multiplicity


def test_3_is_16_multiplicity_8():
    number_n = 16
    number_m = 8
    is_multiplicity = definition_of_multiplicity(number_n, number_m)
    return is_multiplicity


def test_4_is_16_multiplicity_28():
    number_n = 16
    number_m = 28
    is_multiplicity = definition_of_multiplicity(number_n, number_m)
    return not is_multiplicity


def test_suite():
    msg = f"test_1_is_6_multiplicity_3 = {test_1_is_6_multiplicity_3()}"
    msg += f"\ntest_2_is_12_multiplicity_6 = {test_2_is_12_multiplicity_6()}"
    msg += f"\ntest_3_is_16_multiplicity_8 = {test_3_is_16_multiplicity_8()}"
    msg += f"\ntest_4_is_16_multiplicity_28 = {test_4_is_16_multiplicity_28()}"

    print(msg)


test_suite()
main()
