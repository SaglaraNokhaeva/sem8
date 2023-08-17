# Задание №6
# Напишите функцию, которая преобразует pickle файл хранящий список словарей
# в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import pickle


def csv_converter(file):
    with (open(file, 'rb') as file_inp,
          open(f'{file[:-7]}.csv', 'w') as file_out):
        data = pickle.load(file_inp)
        head = data.keys()
        import csv
        writer = csv.writer(file_out, delimiter=';')
        writer.writerow(head)
        for key, values in data.items():
            a, b = tuple(*values.values())
            writer.writerow([*(values.keys()), a, b])


csv_converter('names.pickle')
