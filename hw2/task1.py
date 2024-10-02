#task1
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])

print(f"Первый список: {list1}")
print(f"Второй список: {list2}")
print(f"Поочередное объединение элементов списков: {result}")
