# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def file_transform_to_json(filename):
    with (open(filename, 'r', encoding='utf-8') as file1,
    open(f'{filename}.json', 'w', encoding='utf-8') as file2):
        data = file1.readlines()
        list_to_save = []
        for line in data:
            key, value = line.strip().split(' ')
            list_to_save.append((key.title(), value))
        json.dump(list_to_save, file2, ensure_ascii=False, indent=2)
    print(data)






filename = 'res.txt'
file_transform_to_json(filename)
