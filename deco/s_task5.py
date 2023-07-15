""" Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
 - декораторами для сохранения параметров,
 - декоратором контроля значений и
 - декоратором для многократного запуска.
Выберите верный порядок декораторов """

from .s_task2 import validate_range
from .s_task3 import save_to_json
from .s_task4 import run_multiple_times
import random

@run_multiple_times(3)
@validate_range
@save_to_json
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
    return number

if __name__ == '__main__':
    max_number = int(input("Введите число 1 до 100 для загадывания: "))
    attempts = int(input("Введите количество попыток от 1 до 10: "))
    guessing_game(max_number, attempts)
