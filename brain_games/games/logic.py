import prompt


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
