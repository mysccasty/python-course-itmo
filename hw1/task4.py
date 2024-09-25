#task4
numbers = [num for num in range(1, 61) if num % 2 != 0]

print("Числа, делящиеся на 3 или на 5 и не делящиеся на 15: ")
for num in numbers:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        print(num)

print("Последний элемент списка: ", numbers[-1])
