"""1) Необходимо написать программу, которая находит количество полных секунд
(или минут, или часов), прошедших с начало суток"""


def convert_time(time, style):
    hours, minutes, sec = map(int, time.split(":"))

    if style == "h":
        second_time_in_sec = hours * 60 * 60 + minutes * 60 + sec
        second_time_in_minutes = second_time_in_sec // 60
        second_time_in_hours = second_time_in_minutes // 60
        return second_time_in_hours
    elif style == "m":
        second_time_in_sec = hours * 60 * 60 + minutes * 60 + sec
        second_time_in_minutes = second_time_in_sec // 60
        return second_time_in_minutes
    elif style == "s":
        second_time_in_sec = hours * 60 * 60 + minutes * 60 + sec
        return second_time_in_sec

    return "Error"


def mein():
    first_time = 0
    second_time = (input("Input hours, minutes and seconds in format hh:mm:ss: "))
    style_h_m_s = input("Input h, m or s: ")

    second_time_in_style = convert_time(second_time, style_h_m_s)

    msg = f"{second_time_in_style}, {style_h_m_s}"

    print(msg)


mein()
