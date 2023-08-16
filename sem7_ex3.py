# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
import itertools

names_size = len(list(1 for _ in open('names.txt')))
nums_size = len(list(1 for _ in open('numbers.txt')))
count = max(nums_size, names_size)
with open('res.txt', 'a', encoding='utf-8') as res, \
        open('names.txt', 'r', encoding='utf-8') as names, \
        open('numbers.txt', 'r', encoding='utf-8') as numbers:
    names_str = itertools.cycle(names.readlines())
    # print(names_str)
    numbers_str = itertools.cycle(numbers.readlines())
    # print(numbers_str)
    for i in range(count):
        number_str1, number_str2 = next(numbers_str).split('|')
        prod = float(number_str1) * float(number_str2)
        if prod < 0:
            res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
        else:
            res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')
