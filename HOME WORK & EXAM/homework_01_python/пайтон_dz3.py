# 3. Дана длина ребра куба.
# Найти объем куба и площадь его боковой поверхности.

cube=float(input("Пожалуйста, введите чему равна\nсторона Вашего куба? "))

volume=cube**3

s=4*(cube**2)

print("Объем Вашего куба равен: "+str(volume))

print("А площадь его боковой\nповерхности: "+str(s))