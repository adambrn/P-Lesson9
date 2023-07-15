""" Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции """

import json
import os
from functools import wraps

def save_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        filename = f"{func.__name__}.json"

        data = {}
        if os.path.exists(filename):
            with open(filename, "r", encoding='utf-8') as file:
                data = json.load(file)
        
        result =func(*args, **kwargs)
        data[len(data) + 1] = {"args": args, 
                               "kwargs": kwargs, 
                               "result": result,}

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return result

    return wrapper

if __name__ == '__main__':
    
    @save_to_json
    def multiply_numbers(a, b):
        return a * b
    
    @save_to_json
    def summ_numbers(a, b):
        return a + b
    
    print(multiply_numbers(5, 7)) 
    print(multiply_numbers(3, 4))
    print()
    print(summ_numbers(5, 7)) 
    print(summ_numbers(3, 4))
     
