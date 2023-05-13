"""
4) Even/Odd Vector Values [чётные/нечётные значения вектора]. Написать про-
грамму, которая подсчитывает количество только чётных/нечётных элементов
вектора.
"""


def count_even_values(ls):
    count = 0

    for item in ls:
        if item % 2 == 0:
            count += 1

    return count


def count_odd_values(ls):
    count = 0

    for item in ls:
        if item % 2 != 0:
            count += 1

    return count


def test():
    print(count_even_values([1, 2, 3, 4]) == 2)
    print(count_even_values([2, 4, 6, 8]) == 4)
    print(count_even_values([1, 3, 5, 7]) == 0)


def test_1():
    ls = [1, 2, 3, 4]
    count_even = count_even_values(ls)
    count_odd = count_odd_values(ls)
    return count_even == 2 and count_odd == 2


def test_2():
    ls = [2, 4, 6, 8]
    count_even = count_even_values(ls)
    count_odd = count_odd_values(ls)
    return count_even == 4 and count_odd == 0


def test_3():
    ls = [1, 3, 5, 7]
    count_even = count_even_values(ls)
    count_odd = count_odd_values(ls)
    return count_even == 0 and count_odd == 4


def test_4():
    ls = [11, 13, 15, 17]
    count_even = count_even_values(ls)
    count_odd = count_odd_values(ls)
    return count_even == 0 and count_odd == 4


def test_5():
    ls = [2, 4, 6, 8, 18]
    count_even = count_even_values(ls)
    count_odd = count_odd_values(ls)
    return count_even == 5 and count_odd == 0


def test_suite():
    msg = f"""
       test_1 = {test_1()}
       test_2 = {test_2()}
       test_3 = {test_3()}
       test_4 = {test_4()}
       test_5 = {test_5()}
       """
    print(msg)


def main():
    count = int(input("Enter count of values for vector: "))
    vector = []
    for index in range(0, count):
        vector.append(int(input(f"Enter the vector's value {index}: ")))

    count_even = count_even_values(vector)
    count_odd = count_odd_values(vector)
    print(f"""
    Count Even vector values: {count_even}"
    Count Odd vector values: {count_odd}"
    """)


if __name__ == '__main__':
    test_suite()
    main()
