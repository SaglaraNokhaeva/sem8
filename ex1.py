# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def file_transform_to_json1(filename):
    with (open(filename, 'r', encoding='utf-8') as file1,
    open(f'{filename}.json', 'w', encoding='utf-8') as file2):
        data = file1.readlines()
        list_to_save = []
        for line in data:
            key, value = line.strip().split(' ')
            list_to_save.append((key.title(), value))
        json.dump(list_to_save, file2, ensure_ascii=False, indent=2)
    print(data)


def file_transform_to_json2(filename):
    with (open(filename, 'r', encoding='utf-8') as file1,
    open(f'{filename}2.json', 'w', encoding='utf-8') as file3):
        data = file1.readlines()
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(' ')
            if key.title() in dict_to_save.keys():
                dict_to_save[key.title()].append(value)
            else:
                dict_to_save[key.title()] = [value]
        json.dump(dict_to_save, file3, ensure_ascii=False, indent=2)
    print(data)





filename = 'res.txt'
file_transform_to_json1(filename)
file_transform_to_json2(filename)
