import random


def guess(x):
    random_number = random.randint(1, x)
    _guess = 0
    while _guess != random_number:
        _guess = int(input(f"Guess a number between 1 and {x}: "))
        if _guess < random_number:
            print("Sorry, guess again. Too low.")
        elif _guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")


guess(20)
