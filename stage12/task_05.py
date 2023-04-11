"""
The Exam Results [результаты экзамена]. Необходимо написать программу, ко-
торая обрабатывает результаты экзамена. Для экзамена используется пяти-
балльная система оценивания знаний. Для каждой оценки программа должна
вычислить процент от общего количества оценок. Далее приведен рекомен-
дуемый вид экрана программы
"""


def process_exam_results(marks):
    # count the number of each grade
    count = {
        "fives": 0,
        "fours": 0,
        "triplets": 0,
        "deuces": 0,
        "units": 0,
        "zeros": 0,
    }

    for mark in marks:
        if mark == 5:
            count["fives"] += 1
        elif mark == 4:
            count["fours"] += 1
        elif mark == 3:
            count["triplets"] += 1
        elif mark == 2:
            count["deuces"] += 1
        elif mark == 1:
            count["units"] += 1
        else:
            count["zeros"] += 1

    # calculate the percentage of each grade
    total = len(marks)

    percents = {
        "fives": round(count['fives'] / total * 100, 1),
        "fours": round(count['fours'] / total * 100, 1),
        "triplets": round(count['triplets'] / total * 100, 1),
        "deuces": round(count['deuces'] / total * 100, 1),
        "units": round(count['units'] / total * 100, 1),
        "zeros": round(count['zeros'] / total * 100, 1),
    }

    return count, percents


def test_1():
    marks = list(map(int, "5 4 4 5 3 4 3 4 5 3 4 4 3 4 4 3 5 3 3 4 5 5 5 5 4 5 5 5 2 5".split()))
    (count, percents) = process_exam_results(marks)

    return all([
        count["fives"] == 12,
        count["fours"] == 10,
        count["triplets"] == 7,
        count["deuces"] == 1,
        count["units"] == 0,
        count["zeros"] == 0
    ])


def test_suite():
    msg = f"""
       test_1 = {test_1()}
       """
    print(msg)


def main():
    marks = list(map(int, input("Marks: ").split()))
    (count, percents) = process_exam_results(marks)
    for grade, percent in percents.items():
        print(f"{grade} - {percent}% ({count[grade]})")


if __name__ == '__main__':
    test_suite()
    main()
