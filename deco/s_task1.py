""" Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания и от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. """
import random

def create_guessing_game():
    
    number_max = int(input("Введите число 1 до 100 для загадывания: "))
    while number_max < 1 or number_max > 100:
        print("Число должно быть от 1 до 100.")
        number = int(input("Введите число 1 до 100 для загадывания:"))
    number= random.randint(1,number_max)

    attempts = int(input("Введите количество попыток от 1 до 10: "))
    while attempts < 1 or attempts > 10:
        print("Количество попыток должно быть от 1 до 10.")
        attempts = int(input("Введите количество попыток от 1 до 10: "))

    def guessing_game():
            nonlocal number, attempts
            for attempt in range(attempts):
                guess = int(input(f"Угадайте число от 1 до {number_max}: "))
                if guess == number:
                    print("Поздравляю, вы угадали число!")
                    return
                elif guess < number:
                    print("Загаданное число больше.")
                else:
                    print("Загаданное число меньше.")
            print("Количество попыток исчерпано. Загаданное число:", number)

    return guessing_game

if __name__ == '__main__':
    game = create_guessing_game()
    game()


