class ComputerStatCalculator:

    @staticmethod
    def get_total_amount(ls):
        total_amount = 0
        for item in ls:
            total_amount += item.get_price()
        return total_amount

    @staticmethod
    def get_computer_with_max_price(ls):
        max_computer = ls[0]
        for item in ls:
            if item.get_price() > max_computer.get_price():
                max_computer = item
        return max_computer

    @staticmethod
    def get_computer_with_min_price(ls):
        min_computer = ls[0]
        for item in ls:
            if item.get_price() < min_computer.get_price():
                min_computer = item
        return min_computer
