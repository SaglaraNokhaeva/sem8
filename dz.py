# Задание
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import json
import os

def my_func(source_direct):
    with open(f'result.json', 'w', encoding='utf-8') as file:
        my_dict = {}
        res = []
        for dir_path, dir_name, file_name in os.walk(source_direct):
            # print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n{os.path.abspath(os.path.join(dir_path, os.pardir)) = }\n')
            if dir_path not in my_dict:
                my_dict[dir_path] = file_name
                # my_list.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
        print(my_dict)
        for key, value in my_dict.items():
            res.extend([key, 'directiry'])
            for i in range(len(value)):
                res.extend([value[i], 'file'])

        json.dump(res, file, ensure_ascii=False, indent=2)
            # json.dump('\n', file, ensure_ascii=False)






        # with open(f'result.json', 'w', encoding='utf-8') as file:
        #     my_list = []
        #     for dir_path, dir_name, file_name in os.walk(source_direct):
        #         # print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n{os.path.abspath(os.path.join(dir_path, os.pardir)) = }\n')
        #         if dir_path not in my_list:
        #             my_list.append(dir_path)
        #             # my_list.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
        #         print(my_list)
        #         # file.write('\n'.join(dir_path))
        #         json.dump(dir_path, file, ensure_ascii=False)
        #         # json.dump('\n', file, ensure_ascii=False)


        # if os.path.isfile


my_func('venv')
