# 2. Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.


import os

def rename_files(directory, desired_name, original_extension, final_extension):
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    file_count = 0

    for file_name in os.listdir(directory):
        if file_name.endswith(original_extension):
            file_count += 1

            original_path = os.path.join(directory, file_name)
            new_name = f"{desired_name}{file_count}.{final_extension}"
            new_path = os.path.join(directory, new_name)

            os.rename(original_path, new_path)
            print(f"File '{file_name}' renamed to '{new_name}'.")

    if file_count == 0:
        print(f"No files with '{original_extension}' extension found in '{directory}'.")

# Пример использования функции
rename_files("my_directory", "new_file", ".txt", "docx")
