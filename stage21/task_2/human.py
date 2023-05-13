class Human:

    def __init__(self,
                 first_name="",
                 surname="",
                 age=0,
                 alive=True,
                 ) -> None:
        super().__init__()
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.alive = alive

    def get_first_name(self):
        return self.first_name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def is_alive(self):
        return self.alive

    def is_adult(self):
        return self.age >= 18

    def __str__(self) -> str:
        return f"Human: \n" \
               f"first_name = {self.get_first_name()}, " \
               f"surname = {self.get_surname()}, " \
               f"age = {self.get_age()}, " \
               f"is_alive = {self.is_alive()}, " \
               f"is_adult = {self.is_adult()}"
