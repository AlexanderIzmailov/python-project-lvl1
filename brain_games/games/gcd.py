from random import randint
from brain_games.games.logic import take_name, result, gcd


def gcd_game():
    name = take_name()
    print("Find the greatest common divisor of given numbers.")

    i = 0
    while i != 3:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        correct = gcd(number1, number2)

        if result(correct, str(number1) + " " + str(number2), name):
            i += 1
        else:
            return

    print("Congratulations, " + name + "!")
