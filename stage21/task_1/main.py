"""
1) Необходимо реализовать программный компонент, эмулирующий зебру
(zebra). Данный компонент должен иметь небольшое поведение в виде ме-
тода get_stripe(), который исходя из внутреннего состояния объект должен
выдавать последовательно или строку «black line» (чёрная полоска), или
строку «white line» (белая полоска) при своём однократном вызове на зебра-
объекте. Метод после создания объекта всегда должен первым выдавать
строку «black line». Далее необходимо написать небольшую программу, ко-
торая бы создавала пару зебр-объектов и демонстрировала работу основ-
ного поведения данных объектов.
"""
from zebra import Zebra


def test_1_call_triple_times():
    zebra1 = Zebra()
    return all([
        zebra1.get_stripe() == "black line",
        zebra1.get_stripe() == "white line",
        zebra1.get_stripe() == "black line",
    ])


def test_suite():
    msg = f"""
     test_1_call_twice = {test_1_call_triple_times()}
    """
    print(msg)


def main():
    zebra1 = Zebra()
    zebra2 = Zebra()

    msg = ""
    for index in range(0, 10):
        msg += f"Call number {index + 1} for zebra1 - {zebra1.get_stripe()}\n"
        msg += f"Call number {index + 1} for zebra2 - {zebra2.get_stripe()}\n"

    print(msg)


if __name__ == '__main__':
    test_suite()
    main()
