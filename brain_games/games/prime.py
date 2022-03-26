from brain_games.games.logic import take_name, result, prime
from random import randint


def prime_game():
    name = take_name()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    i = 0
    while i != 3:
        number = randint(1, 100)
        correct = prime(number)

        if result(correct, number, name):
            i += 1
        else:
            return

    print("Congratulations, " + name + "!")
