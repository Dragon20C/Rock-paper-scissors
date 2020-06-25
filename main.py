import random

list = ["rock", "paper", "scissors"]

while True:
    options = random.choice(list)
    player = input("rock:1 paper:2 scissors:3 : ")
    if player == "1" and options == "rock":
        print("Draw")
    elif player == "1" and options == "paper":
        print("Lose")
    elif player == "1" and options == "scissors":
        print("Win")
    if player == "2" and options == "rock":
        print("Win")
    elif player == "2" and options == "paper":
        print("Draw")
    elif player == "2" and options == "scissors":
        print("Lose")
    if player == "3" and options == "rock":
        print("Lose")
    elif player == "3" and options == "paper":
        print("Win")
    elif player == "3" and options == "scissors":
        print("Draw")

    print("Bot chose: " + options)