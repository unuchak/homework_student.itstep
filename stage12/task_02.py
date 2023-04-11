"""
2) The Mirror Vector [зеркальный вектор]. Необходимо разработать программу,
которая проверяет, что все элементы вектора расположены в зеркальном
виде относительно его середины.
"""


def check_mirror(ls):
    num = len(ls) // 2
    for index in range(num):
        if ls[index] != ls[len(ls) - 1 - index]:
            return False

    return True


def test_1_12321():
    return check_mirror([1, 2, 3, 2, 1])


def test_2_123321():
    return check_mirror([1, 2, 3, 3, 2, 1])


def test_3_14321():
    return not check_mirror([1, 4, 3, 2, 1])


def test_4_12324():
    return not check_mirror([1, 2, 3, 2, 4])


def test_suite():
    msg = f"""
       test_1_12321 = {test_1_12321()}
       test_2_123321 = {test_2_123321()}
       test_3_14321 = {test_3_14321()}
       test_4_12324 = {test_4_12324()}
       """
    print(msg)


def main():
    count = int(input("Enter count of values for vector: "))
    vector = []
    for index in range(0, count):
        vector.append(int(input(f"Enter the vector's value {index}: ")))

    is_mirrored = check_mirror(vector)
    print(f"Are vector values mirrored? - {is_mirrored}")


if __name__ == '__main__':
    test_suite()
    main()
