#task3
numbers = []
list_sum = 0
print("Введите число (для завершения ввода -1): ")
while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)
    list_sum += num

print("Длина списка: ", len(numbers))
print("Сумма элементов в списке (через цикл): ", list_sum)
print("Сумма элементов в списке (через метод списка): ", sum(numbers))

even_numbers = [num for num in numbers if num % 2 == 0]
print("Четные элементы: ", even_numbers)