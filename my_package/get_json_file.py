import json
import os
from my_package import get_dir_size

def my_func(source_dir):
    res = {}
    for path, dirs, files in os.walk(source_dir):
        # print(path, get_dir_size(path), os.path.abspath(os.path.join(path, os.pardir)))
        res[path] = ['directory', get_dir_size(path), os.path.abspath(os.path.join(path, os.pardir))]
        for f in files:
            # print(path, f, os.path.getsize(os.path.join(path, f)), path)
            res[f] = ['file',os.path.getsize(os.path.join(path, f)), path]
    # print(res)
    with open(f'result.json', 'w', encoding='utf-8') as file:
        json.dump(res, file, indent=2)