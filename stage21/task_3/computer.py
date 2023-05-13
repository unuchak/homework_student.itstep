class Computer:

    def __init__(self,
                 brand="",
                 model="",
                 price=0.0,
                 ) -> None:
        super().__init__()
        self.__brand = brand
        self.__model = model
        self.__price = price

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self) -> str:
        return f"Computer: " \
               f"brand = {self.get_brand()}, " \
               f"model = {self.get_model()}, " \
               f"price = {self.get_price()} BYN"
