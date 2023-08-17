import csv
import json
import os


def my_csv():

    with (open('result.json', 'r') as f1,
          open('result.csv', 'w', encoding='utf-8', newline='') as file):

        data = json.load(f1)
        print(data)
        columns = ['object', 'file or dir', 'size', 'parent_dir']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(columns)
        result = []
        for key, value in data.items():
            result.append([key, *data[key]])
            # result.extend([value])
            # result.append(value)
            # for i in data[key]:
            #     result.append(*i)
        writer.writerows(result)


my_csv()
