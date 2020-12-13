import random


def play():
    user = input("Rock, Paper, Scissor \n'r' for Rock\n'p' for Paper\n's' for Scissor:\n ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It\'s a tie"

    if is_win(user, computer):
        return "You won!"

    return "you Lost!"


def is_win(player, opponent):
    # returns true if player wins
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        return True


print(play())
