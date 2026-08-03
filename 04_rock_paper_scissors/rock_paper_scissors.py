import random

choices = ["rock", "paper", "scissors"]
print("====== Rock Paper Scissors ======")

print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice = int(input("Enter your choice: "))

player_choice = choices[choice-1]
print(player_choice)

computer_choice = random.choice(choices)
print(f"Computer Choice : {computer_choice}")