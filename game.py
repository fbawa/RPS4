# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# Capture inputs

user_choice = input("Please choose one of the following options: 'rock, 'paper', or 'scissors':")

print("-----------")
print("Selected:", user_choice)

# Validate INPUTS

options = ["rock", "paper", "scissors"]

if user_choice in (options)                            :
    pass
else:
    print("Invalid selection, please try again")
    exit()

# Generate computer selection


computer_choice = random.choice(options)

print("-------------")
print("Generating...")
print("Computer Choice:", computer_choice)

# Determine the winner

if user_choice == computer_choice:
    print("tie")

elif user_choice == "rock" and computer_choice == "paper":
    print("paper")
elif user_choice == "rock" and computer_choice == "scissors":
    print ("rock")
elif user_choice == "paper" and computer_choice == "scissors":
    print ("scissors")


#rock beats scissors
#paper beats rock
#scissors beats paper
#same selection is a tie


# Display final outputs / outcome