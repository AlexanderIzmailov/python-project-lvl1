from random import randint
from brain_games.games.logic import take_name, result


def even_game():
    name = take_name()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    i = 0
    while i != 3:
        number = randint(0, 100)
        is_even = "yes" if number % 2 == 0 else "no"

        if result(is_even, number, name):
            i += 1
        else:
            return

    print("Congratulations, " + name + "!")
