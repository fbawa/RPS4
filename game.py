# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# Capture inputs

user_choice = input("Please choose one of the following options: 'rock, 'paper', or 'scissors':")

print("-----------")
print("Selected:", user_choice)

# Validate INPUTS

if user_choice in ["rock", "paper", "scissors"]                            :
    pass
else:
    print("Invalid selection, please try again")
    exit()

# Generate computer selection

print("Generating...")


computer_choice = random.choice(["rock", "paper", "scissors"])

print("Computer Choice:", computer_choice)

# Determine the winner






# Display final outputs / outcomes