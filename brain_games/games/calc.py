from random import randint
from brain_games.games.logic import take_name, result


def calc_game():
    name = take_name()
    print("What is the result of the expression?")

    i = 0
    while i != 3:
        x = randint(0, 100)
        y = randint(0, 100)
        operation = randint(0, 2)

        if operation == 0:
            qst = str(x) + " + " + str(y)
            correct = x + y
        elif operation == 1:
            qst = str(x) + " - " + str(y)
            correct = x - y
        else:
            qst = str(x) + " * " + str(y)
            correct = x * y

        if result(correct, qst, name):
            i += 1
        else:
            return
    print("Congratulations, " + name + "!")
