""" Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-
угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов """

import random
from functools import wraps

def validate_range(func):

    @wraps(func)
    def wrapper(max_number, attempts):
        if not (1 <= max_number <= 100) or not (1 <= attempts <= 10):
            max_number = random.randint(1, 100)
            attempts = random.randint(1, 10)
            print("Параметры не входят в указанные диапазоны. Используются случайные числа.")

        return func(max_number, attempts)

    return wrapper

@validate_range
def guessing_game(max_number, attempts):
    number = random.randint(1, max_number)
    for _ in range(attempts):
        guess = int(input(f"Угадайте число от 1 до {max_number}: "))
        if guess == number:
            print("Поздравляю, вы угадали число!")
            return
        elif guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    print("Количество попыток исчерпано. Загаданное число:", number)


if __name__ == '__main__':
    max_number = int(input("Введите число 1 до 100 для загадывания: "))
    attempts = int(input("Введите количество попыток от 1 до 10: "))
    guessing_game(max_number, attempts)

