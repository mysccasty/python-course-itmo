#task2
persons = [('John', 20), ('Nick', 15), ('Kate', 25)]

filtered_persons = sorted([t for t in persons if t[1] > 18], key=lambda t: t[1], reverse=True)

print(f"Список имен и возрастов людей: {persons}")
print(f"Отфильтрованный и отсортированный по возрасту список: {filtered_persons}")

