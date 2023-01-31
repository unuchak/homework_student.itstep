# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 3) N белочек нашли K орешков и решили разделить их поровну. Необходимо
# разработать программу, которая определяет, сколько орешков достанется
# каждой белочке. Дополнительно определите, сколько орешков останется по-
# сле того, как все белочки возьмут себе равное количество орешков.

amount_of_squirrels = int(input("Input amount of squirrels: "))
amount_of_nuts = int(input("Input amount of nuts: "))

result, remainder = divmod(amount_of_nuts, amount_of_squirrels)

msg = f"""Will get every squirrel: {result}
Nuts will remain: {remainder}"""

print(msg)
