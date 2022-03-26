from brain_games.games.logic import take_name, result, progression


def progression_game():
    name = take_name()
    print("What number is missing in the progression?")

    i = 0
    while i != 3:
        qst, hidden = progression()

        if result(hidden, qst, name):
            i += 1
        else:
            return

    print("Congratulations, " + name + "!")
