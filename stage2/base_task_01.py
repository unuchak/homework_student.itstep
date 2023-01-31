# Version 1.0
# Author: marina.unuchak
# Date: 29.01.2023

# 1) Для закрепления написания простейших консольных интерактивных про-
# грамм с использованием языка Python попробуйте создать простенькие
# программы-конверторы для различных шкал температур (из градусов Цель-
# сия в градусы Фаренгейта или Кельвина и наоборот) или для различных ва-
# лют (к примеру, из бел. руб. в евро или наоборот). Можно использовать лю-
# бую предметную область для создания однотипных приложений (к примеру,
# конвертор значений углов из градусы в радианы и наоборот и т.д.).

amount_byn = float(input("Input any amount in BYN: \n"))
exchange_byn_to_dollar_sale = 2.6690
exchange_byn_to_dollar_buy = 2.6010

amount_dollar_buy, balance_after_buy = divmod(amount_byn, exchange_byn_to_dollar_buy)

balance_in_byn = int(balance_after_buy)
balance_in_kopecks = int((balance_after_buy - balance_in_byn) * 100)

msg = f"""Exchange rates bel.rub to dollar 
Buy: {exchange_byn_to_dollar_buy}
Sale: {exchange_byn_to_dollar_sale}
Result: {amount_dollar_buy} $
Odd money: {balance_in_byn} BYN {balance_in_kopecks} kopecks
"""

print(msg)
