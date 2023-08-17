import json
import os


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


res = {}
for path, dirs, files in os.walk('venv'):
    print(path, get_dir_size(path), os.path.abspath(os.path.join(path, os.pardir)))
    res[path] = ['directory', get_dir_size(path), os.path.abspath(os.path.join(path, os.pardir))]
    for f in files:
        print(path, f, os.path.getsize(os.path.join(path, f)), path)
        res[f] = ['file',os.path.getsize(os.path.join(path, f)), path]
print(res)
with open(f'result2.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=2)

