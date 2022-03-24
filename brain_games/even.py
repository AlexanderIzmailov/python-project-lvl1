from random import randint
import prompt


def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    i = 0
    while i != 3:
        number = randint(0, 100)
        is_even = "yes" if number % 2 == 0 else "no"
        print("Question: " + str(number))
        answer = prompt.string('Your answer: ')

        if answer != is_even:
            print(f"'{answer}' is wrong answer ;(. ", end="")
            print(f"Correct answer was '{is_even}'.")
            print("Let's try again, " + name + "!")
            return()
        else:
            print("Correct!")
            i += 1

    print("Congratulations, " + name + "!")
