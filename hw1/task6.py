#task6
import numpy as np

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("У данного уравнения нет натуральных корней.")
elif D == 0:
    x = -b / (2 * a)
    print(f"У данного уравнения один корень: {x}")
else:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(f"У данного уравнения два корня: {x1} и {x2}")

solutions = np.roots([a, b, c])
print("Корни уравнения с numpy: ", solutions)


