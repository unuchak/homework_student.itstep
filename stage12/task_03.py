"""
3) Vector with the Same/Different Values [вектор с одинаковыми/разными зна-
чениями]. Необходимо разработать программу, которая проверяет, что все
элементы вектора различны/одинаковы.
"""


def check_all_the_same(ls):
    first = ls[0]

    for item in ls:
        if first != item:
            return False

    return True


def test_1_11111():
    return check_all_the_same([1, 1, 1, 1, 1])


def test_2_2222():
    return check_all_the_same([2, 2, 2, 2])


def test_3_010():
    return not check_all_the_same([0, 1, 0])


def test_suite():
    msg = f"""
       test_1_11111 = {test_1_11111()}
       test_2_2222 = {test_2_2222()}
       test_3_010 = {test_3_010()}
       """
    print(msg)


def main():
    count = int(input("Enter count of values for vector: "))
    vector = []
    for index in range(0, count):
        vector.append(int(input(f"Enter the vector's value {index}: ")))

    is_mirrored = check_all_the_same(vector)
    print(f"Are vector values the same? - {is_mirrored}")


if __name__ == '__main__':
    test_suite()
    main()
