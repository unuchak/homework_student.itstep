"""
Version 1.0
Author: marina.unuchak
Date: 5.01.2023
3) Даны значения двух моментов времени, принадлежащих одним и тем же сут-
кам: часы, минуты и секунды для каждого из моментов времени. Известно, что
второй момент времени наступил не раньше первого. Определите, сколько
секунд прошло между двумя моментами времени
"""

first_time = (input(":Input hours, minutes and seconds in format hh:mm:ss : "))  # 12:34:56
second_time = (input("Input hours, minutes and seconds in format hh:mm:ss : "))  # 23:14:32

first_time_hh, first_time_mm, first_time_ss = map(int, first_time.split(":"))
second_time_hh, second_time_mm, second_time_ss = map(int, second_time.split(":"))

first_time_sec = first_time_hh * 60 * 60 + first_time_mm * 60 + first_time_ss
second_time_sec = second_time_hh * 60 * 60 + second_time_mm * 60 + second_time_ss

diff_time_sec = second_time_sec - first_time_sec

msg = f"""Seconds elapsed between two times {diff_time_sec} sec"""

print(msg)
