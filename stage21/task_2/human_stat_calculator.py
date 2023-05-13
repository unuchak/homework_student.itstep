class HumanStatCalculator:

    @staticmethod
    def get_alive_count(ls):
        alive_count = 0
        for item in ls:
            if item.is_alive():
                alive_count += 1
        return alive_count

    @staticmethod
    def get_not_alive_count(ls):
        return len(ls) - HumanStatCalculator.get_alive_count(ls)

    @staticmethod
    def get_adult_count(ls):
        adult_count = 0
        for item in ls:
            if item.is_adult():
                adult_count += 1
        return adult_count

    @staticmethod
    def get_not_adult_count(ls):
        return len(ls) - HumanStatCalculator.get_adult_count(ls)
