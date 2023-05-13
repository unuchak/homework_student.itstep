"""
3) Необходимо реализовать программный компонент, эмулирующий компью-
тер (computer) или ноутбук (laptop). Минимум программный компонент дол-
жен содержать следующие параметры: бренд (brand), модель (model) и цену
(price). Остальные параметры можно выбрать самостоятельно исходя из бу-
дущей логики программной системы. Доступ к соответствующим полям ор-
ганизовать через соответствующие свойства. Также у программного компо-
нента должны быть реализованы конструктор и метод __str__(...) для пред-
ставления состояния объекта в виде строки. Далее требуется написать не-
большую программу, которая бы создавала пару компьютеров с различ-
ными параметрами и определяла общую стоимость всех компьютеров, а
также находила самый дорогой и дешёвый компьютеры
"""
from computer import Computer
from computer_stat_calculator import ComputerStatCalculator


def test_1_get_total_amount():
    ls = [
        Computer(price=10),
        Computer(price=28),
    ]

    return ComputerStatCalculator.get_total_amount(ls) == 30


def test_2_get_computer_with_max_price():
    ls = [
        Computer(price=10),
        Computer(price=20)
    ]
    computer_with_max_price = ComputerStatCalculator.get_computer_with_max_price(ls)
    return computer_with_max_price.get_price() == 20


def test_3_get_computer_with_max_price():
    ls = [
        Computer(price=10),
        Computer(price=28)
    ]
    computer_with_min_price = ComputerStatCalculator.get_computer_with_min_price(ls)
    return computer_with_min_price.get_price() == 10


def test_suite():
    msg = f"""
     test_1_get_total_amount = {test_1_get_total_amount()}
     test_2_get_computer_with_max_price = {test_2_get_computer_with_max_price()}
     test_3_get_computer_with_max_price = {test_3_get_computer_with_max_price()}
    """
    print(msg)


def main():
    ls = [
        Computer(brand="Acer", model="SpaceX", price=2800.68),
        Computer(brand="Mac", model="2", price=3500.50),
        Computer(brand="Asus", model="Travel", price=1500.0),
        Computer(brand="HP", model="5600", price=1500.1)
    ]

    msg_stat = f"""Statistic result:
    Total amount: {ComputerStatCalculator.get_total_amount(ls)} BYN
    Computer with Max price: {ComputerStatCalculator.get_computer_with_max_price(ls)} 
    Computer with Min price: {ComputerStatCalculator.get_computer_with_min_price(ls)}
    """
    print(msg_stat)


if __name__ == '__main__':
    test_suite()
    main()
