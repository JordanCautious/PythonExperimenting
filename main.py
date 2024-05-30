# This is a testing ground for Python code

# Practice with Rock, Paper, Scissors in Python
import random

while True:
    choices = ["Rock", "Paper", "Scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper, or Scissors?: ").capitalize()

    print(f"The computer chose {computer}!")
    print(f"The player chose {player}!")

    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer wins!")
        elif computer == "Scissors":
            print("Player wins!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer wins!")
        elif computer == "Rock":
            print("Player wins!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer wins!")
        elif computer == "Paper":
            print("Player wins!")

    play_again = input("Play again? (Y/N): ").capitalize()

    if play_again != "Y":
        break

print("Bye!")
