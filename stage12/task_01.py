"""
1) Vector of Ordered Values [вектор упорядоченный значений]. Необходимо раз-
работать программу, которая проверяет, что все элементы вектора находятся
в упорядоченном виде, т.е. отсортированы по возрастанию или убыванию.
"""


def check_sort_asc(ls):
    for index in range(len(ls) - 1):
        if ls[index] >= ls[index + 1]:
            return False

    return True


def check_sort_desc(ls):
    for index in range(len(ls) - 1):
        if ls[index] <= ls[index + 1]:
            return False

    return True


def check_ordered(ls):
    return check_sort_asc(ls) or check_sort_desc(ls)


def test_1_123456():
    return check_ordered([1, 2, 3, 4, 5, 6])


def test_2_654321():
    return check_ordered([6, 5, 4, 3, 2, 1])


def test_3_674125():
    return not check_ordered([6, 7, 4, 1, 2, 5])


def test_4_245513():
    return not check_ordered([2, 4, 5, 5, 1, 3])


def test_suite():
    msg = f"""
    test_1_123456 = {test_1_123456()}
    test_2_654321 = {test_2_654321()}
    test_3_674125 = {test_3_674125()}
    test_4_245513 = {test_4_245513()}
    """
    print(msg)


def main():
    count = int(input("Enter count of values for vector: "))
    vector = []
    for index in range(0, count):
        vector.append(int(input(f"Enter the vector's value {index}: ")))

    is_sorted = check_ordered(vector)
    print(f"Are vector values ordered? - {is_sorted}")


if __name__ == '__main__':
    test_suite()
    main()
