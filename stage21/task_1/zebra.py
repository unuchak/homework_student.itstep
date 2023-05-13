class Zebra:
    __COLOR_BLACK = "black"
    __COLOR_WHITE = "white"

    def __init__(self) -> None:
        super().__init__()
        self.__line_index = 0

    def get_stripe(self):
        line_color = self.__get_current_line_color__()
        stripe_text = f"{line_color} line"
        self.__increment_line_index__()
        return stripe_text

    def __increment_line_index__(self):
        self.__line_index = 1 if self.__line_index == 0 else 0

    def __get_current_line_color__(self):
        return self.__COLOR_BLACK if self.__line_index % 2 == 0 else self.__COLOR_WHITE
