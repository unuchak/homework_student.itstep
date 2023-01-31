
# Version 1.0
# Author: marina.unuchak
# Date: 31.01.2023
# 1) Масса динозавра задаётся в граммах. Необходимо разработать программу, ко-
# торая вычисляет, сколько это килограммов (1 кг = 1000 грамм), центнеров (1
# центнер = 100 килограмм) и тонн (1 тонна = 1000 кг).

mass_of_dinosaurs = float(input("Input mass of dinosaurs in grams : \n"))

mass_kilogram = 1000
mass_centners = 100 * mass_kilogram
mass_tons = 1000 * mass_kilogram

result_1 = mass_of_dinosaurs // mass_kilogram
result_2 = mass_of_dinosaurs // mass_centners
result_3 = mass_of_dinosaurs // mass_tons

msg = f"""Mass_of_dinosaurs in grams, {mass_of_dinosaurs}
Mass_of_dinosaurs in kilogram, {result_1}
Mass_of_dinosaurs in centners, {result_2}
Mass_of_dinosaurs in tons, {result_3}"""

print(msg)
