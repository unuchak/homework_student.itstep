# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 2) Дан общий размер файла в байтах (размер задаётся в виде целого числа).
# Необходимо разработать программу, которая вычисляет, сколько это кило-
# байтов (1Кб = 1024 байт), мегабайтов (1Мб = 1024Кб), гигабайтов (1Гб =
# 1024Мб) и терабайтов (1Тб = 1024Гб).

file_in_bytes = int(input("Input file_in_bytes: "))

kilobytes = 1024
megabytes = kilobytes ** 2
gigabytes = kilobytes ** 3
terabytes = kilobytes ** 4

result_1 = file_in_bytes / kilobytes
result_2 = file_in_bytes / megabytes
result_3 = file_in_bytes / gigabytes
result_4 = file_in_bytes / terabytes

msg = f"""File size in bytes, {file_in_bytes}
File size in kilobytes , {result_1}
File size in megabytes, {result_2}
File size in gigabytes, {result_3}
File size in terabytes, {result_4}
"""

print(msg)
