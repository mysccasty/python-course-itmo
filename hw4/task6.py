import os
import shutil
import time
from datetime import datetime
import signal
import sys
import select

stop_flag = False
backup_in_progress = False


def create_backup(source_dir, target_dir):
    global backup_in_progress
    backup_in_progress = True
    print("Начинается процесс резервного копирования...")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(target_dir, f"backup_{timestamp}")

    os.makedirs(backup_dir, exist_ok=True)

    try:
        shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)
        print(f"Резервная копия создана в: {backup_dir}")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")
    finally:
        backup_in_progress = False
        print("Резервное копирование завершено.")


def signal_handler(signum, frame):
    global stop_flag
    if backup_in_progress:
        print("\nРезервное копирование выполняется. Пожалуйста, дождитесь его завершения...")
    else:
        print("\nНажато Ctrl + C. Завершение работы после текущего бэкапа...")
        stop_flag = True


while True:
    source_dir = input("Введите путь к директории для резервирования: ").strip()
    if os.path.isdir(source_dir):
        break

    print("Ошибка: Исходная директория не найдена.")

target_dir = input("Введите путь к директории для сохранения резервных копий: ").strip()
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

while True:
    try:
        interval = int(input("Введите интервал резервного копирования (в секундах): "))
        if interval <= 0:
            raise ValueError
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите положительное целое число.")

print("Скрипт резервного копирования запущен. Для завершения введите 'exit' или нажмите Ctrl + C.")

signal.signal(signal.SIGINT, signal_handler)

try:
    while not stop_flag:
        create_backup(source_dir, target_dir)

        if stop_flag:
            break

        print(f"Ожидание {interval} секунд до следующего резервного копирования.")
        start_time = time.time()

        while time.time() - start_time < interval:
            remaining_time = interval - (time.time() - start_time)
            print(f"Осталось времени до следующего бэкапа: {int(remaining_time)} секунд", end='\r')

            ready, _, _ = select.select([sys.stdin], [], [], 1)
            if ready:
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == 'exit':
                    stop_flag = True
                    break

            time.sleep(1)

finally:
    if backup_in_progress:
        print("Резервное копирование все еще выполняется. Пожалуйста, дождитесь его завершения...")
    while backup_in_progress:
        time.sleep(1)
    print("Скрипт завершен.")
