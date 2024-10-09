# task1
from functools import reduce

print("Введите список чисел(для остановки введите -1):")
numbers = []

while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

print("Введенный список: ", numbers)

cubed_numbers = list(map(lambda x: x**3, numbers))
print("Кубы чисел: ", cubed_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, cubed_numbers))
print("Четные кубы: ", even_numbers)

product = reduce(lambda x, y: x * y, even_numbers)
print("Произведение четных кубов: ", product)
