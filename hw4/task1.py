# task1
import re

def find_emails_and_phone_numbers(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f'Ошибка: Файл "{input_file}" не найден.')
        return
    except IOError as io_err:
        print(f'Ошибка чтения файла: {io_err}')
        return

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}'

    emails = re.findall(email_pattern, text)
    phone_numbers = re.findall(phone_pattern, text)

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('Найденные электронные почты:\n')
            file.write('\n'.join(emails))
            file.write('\n\n')
            file.write('Найденные номера телефонов:\n')
            file.write('\n'.join(phone_numbers))
        print(f'Результаты успешно сохранены в "{output_file}".')
    except IOError as io_err:
        print(f'Ошибка записи в файл: {io_err}')

input_filename = input('Введите имя входного файла: ')
output_filename = input('Введите имя выходного файла: ')
find_emails_and_phone_numbers(input_filename, output_filename)