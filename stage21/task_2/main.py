"""
2) Необходимо реализовать программный компонент человека (human), у ко-
торого обязательно должны быть следующие характеристики: имя (first
name), фамилия (surname), возраст (age) и поле-состояние живой или нежи-
вой (alive). Доступ к соответствующим полям организовать через соответ-
ствующие свойства. В программном компоненте необходимо также реали-
зовать поведение в виде метода, который определял бы, является ли чело-
век совершеннолетним или нет, а также живой ли сейчас этот человек или
его уже нет. Дополнительно у программного компонента должны быть реа-
лизованы конструктор и метод __str__(...) для представления состояния объ-
екта в виде строки. Далее требуется написать небольшую программу, кото-
рая бы создавала пару людей с различными параметрами и определяла
сколько среди людей совершеннолетних, а сколько нет, а также выдавала
статистику по живым и не живым.
"""
from human import Human

from human_stat_calculator import HumanStatCalculator


def test_1_is_adult():
    human = Human(age=18)
    return human.is_adult()


def test_2_is_alive():
    human = Human(alive=True)
    return human.is_alive()


def test_3_get_alive_count():
    ls = [
        Human(alive=True),
        Human(alive=True),
        Human(alive=False)
    ]
    return HumanStatCalculator.get_alive_count(ls) == 2


def test_4_get_alive_count():
    ls = [
        Human(alive=True),
        Human(alive=True),
        Human(alive=False)
    ]
    return HumanStatCalculator.get_not_alive_count(ls) == 1


def test_suite():
    msg = f"""
     test_1_is_adult = {test_1_is_adult()}
     test_2_is_alive = {test_2_is_alive()}
     test_3_get_alive_count = {test_3_get_alive_count()}
     test_4_get_alive_count = {test_4_get_alive_count()}
    """
    print(msg)


def main():
    ls = [
        Human(first_name="Marina", surname="Unuchek", age=28, alive=True),
        Human(first_name="Mary", surname="Bobson", age=35, alive=True),
        Human(first_name="Bob", surname="Stivonson", age=15, alive=True),
        Human(first_name="Andrew", surname="Ivanov", age=15, alive=False)
    ]

    msg_stat = f"""Statistic result:
    alive count: {HumanStatCalculator.get_alive_count(ls)}
    not alive count: {HumanStatCalculator.get_not_alive_count(ls)}
    adult count: {HumanStatCalculator.get_adult_count(ls)}
    not adult count: {HumanStatCalculator.get_not_adult_count(ls)}
    """
    print(msg_stat)


if __name__ == '__main__':
    test_suite()
    main()
