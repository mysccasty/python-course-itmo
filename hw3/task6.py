# task6

def my_hash(string):
    return sum(ord(c) for c in string) % 256


def add_to_table(table, string, index):
    if string in table.get(index, []):
        print("Предупреждение! Строка уже в таблице.")
    else:
        table.setdefault(index, []).append(s)
        print("Строка добавлена в таблицу.")
    return table


def remove_from_table(table, string, index):
    if index in table and string in table[index]:
        table[index].remove(string)
    elif index not in table:
        print("Предупреждение! Индекса нет в таблице.")
    elif string not in table[index]:
        print("Предупреждение! Строка не в таблице.")
    return table


def search_in_table(table, string, index):
    return string in table.get(index, [])


hash_table = {}
while True:
    print("1. Добавить строку", "2. Убрать строку", "3. Поиск строки", "4. Вывести таблицу", "5. Выход", sep="\n")
    choice = input("Выберите действие: ")
    if choice == "1":
        s = input("Введите строку: ")
        hash_index = my_hash(s)
        add_to_table(hash_table, s, hash_index)
    elif choice == "2":
        s = input("Введите строку для удаления: ")
        hash_index = my_hash(s)
        hash_table = remove_from_table(hash_table, s, hash_index)
    elif choice == "3":
        s = input("Введите строку для поиска: ")
        hash_index = my_hash(s)
        print(search_in_table(hash_table, s, hash_index))
    elif choice == "4":
        print(hash_table)
    elif choice == "5":
        break
    else:
        print("Неверный ввод. Повторите ввод.")

