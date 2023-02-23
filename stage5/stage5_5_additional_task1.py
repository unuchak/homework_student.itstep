"""
Необходимо написать программу нахождения количества квадратов со сторо-
ной a, размещённых на прямоугольнике со сторонами b и c, а также площадь
незанятой части прямоугольника.
"""


def calc_count_and_left_square(a, b, c):
    count_on_b = b // a
    count_on_c = c // a
    count = count_on_b * count_on_c
    s_bc = b * c
    s_a = count * a * a
    left_square = s_bc - s_a
    return count, left_square


def main():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))

    count, left_s = calc_count_and_left_square(a, b, c)

    print(f"Count: {count}, left square: {left_s}")


main()
