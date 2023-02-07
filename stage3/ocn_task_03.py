# Version 1.0
# Author: marina.unuchak
# Date: 5.01.2023
# 3) Даны значения двух моментов времени, принадлежащих одним и тем же сут-
# кам: часы, минуты и секунды для каждого из моментов времени. Известно, что
# второй момент времени наступил не раньше первого. Определите, сколько
# секунд прошло между двумя моментами времени

first_time = (input(":Input hours, minutes and seconds in format hh:mm:ss: "))
second_time = (input("Input hours, minutes and seconds in format hh:mm:ss: "))

a, b, c = map(int, first_time.split(":"))
d, i, f = map(int, second_time.split(":"))

first_time_sec = a * 60 * 60 + b * 60 + c
second_time_sec = d * 60 * 60 + i * 60 + f

diff_time_sec = second_time_sec - first_time_sec

msg = f"""Seconds elapsed between two times {diff_time_sec}"""

print(msg)
