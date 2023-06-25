# 1. Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
import random

def generate_random_files(directory, num_files):
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    existing_files = set(os.listdir(directory))

    for i in range(num_files):
        file_name = f"file{i+1}.txt"
        file_path = os.path.join(directory, file_name)
        
        if file_name in existing_files:
            print(f"File '{file_name}' already exists. Skipping.")
            continue

        with open(file_path, "w") as file:
            file.write("Random content.")

        print(f"File '{file_name}' generated successfully.")

# Пример использования функции
generate_random_files("my_directory", 5)


