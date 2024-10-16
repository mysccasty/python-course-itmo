import random
import string


def generate_password(length):
    if length < 1:
        raise ValueError("Длина пароля должна быть положительным целым числом.")

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    return password


try:
    length = int(input("Введите желаемую длину пароля: "))
    password = generate_password(length)
    print(f"Сгенерированный пароль: {password}")

except ValueError as ve:
    print(f"Ошибка: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
