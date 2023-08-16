# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def func():

    with (open('my_file.json', 'r') as f1,
          open('name.csv', 'w', encoding='utf-8', newline='') as file):
        data = json.load(f1)
        columns = ['level', 'pers_id', 'name']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(columns)
        result = []
        for key, value in data.items():
            for i in data[key]:
                result.append([key, i, data[key][i]])
        writer.writerows(result)

func()