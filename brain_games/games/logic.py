import prompt
from random import randint


def take_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def result(correct, question, name):
    print("Question: " + str(question))
    answer = prompt.string('Your answer: ')
    if answer != str(correct):
        print(f"'{answer}' is wrong answer ;(. ", end="")
        print(f"Correct answer was '{correct}'.")
        print("Let's try again, " + name + "!")
        return False
    else:
        print("Correct!")
        return True


def gcd(x, y):
    if x > y:
        bigger = x
        smaller = y
    elif y > x:
        bigger = y
        smaller = x
    else:
        return (x)

    i = 0
    while i <= smaller - 1:
        if smaller % (smaller - i) == 0 and bigger % (smaller - i) == 0:
            return smaller - i
        i += 1
    return ("None")


def progression():
    amount = randint(5, 15)
    step = randint(-10, 10)
    start = randint(-100, 100)
    hidden_position = randint(1, amount)

    result = ""
    next_num = start
    i = 1
    while i <= amount:

        if i == hidden_position:
            result += ".. "
            hidden_num = next_num
        else:
            result += str(next_num) + " "

        next_num += step
        i += 1

    return (result.strip(), hidden_num)


def prime(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return "no"
        i += 1

    return "yes"
