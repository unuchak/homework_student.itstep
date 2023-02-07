# Version 1.0
# Author: marina.unuchak
# Date: 1.01.2023
# 2) Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей
# и копеек нужно заплатить за N пирожков

pie_price_rub = int(input("Input a pie price rub: "))
pie_price_cent = int(input("Input a pie price cents: "))
n = int(input("Input a number of pies: "))

one_pie_price = pie_price_rub + pie_price_cent / 100
total_price = n * one_pie_price
rub = int(total_price)
cent = int((total_price % 1) * 100)
msg = f"""Total Price is: {rub} rub and {cent} cent"""

print(msg)
