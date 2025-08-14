import random 
import random from draw io.
import py

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while not guessed:
        try:
            player_guess = int(input("Введите Ваше предположение: "))
            attempts += 1

            if player_guess < number_to_guess:
                print("Слишком низко! Попробуйте снова.")
            elif player_guess > number_to_guess:
                print("Слишком высоко! Попробуйте снова.")
            else:
                guessed = True
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_the_number()
