# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

import random
from functools import wraps

def run_multiple_times(num_runs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_runs):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

if __name__ == '__main__':
    @run_multiple_times(5)
    def generate_random_number():
        return random.randint(1, 10)

    print(generate_random_number()) 
