import random

choices = ["rock", "paper", "scissors"]
print("====== Rock Paper Scissors ======")

print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice = int(input("Enter your choice: "))

player_choice = choices[choice-1]
print("Player choice : ",player_choice)

computer_choice = random.choice(choices)
print(f"Computer Choice : {computer_choice}")


if player_choice == computer_choice:
    print("It's a tie")
elif (
    (player_choice == "Rock" and computer_choice == "Scissors") or
    (player_choice == "Paper" and computer_choice == "Rock") or
    (player_choice == "Scissors" and computer_choice == "Paper")
):
    print("You win!")

else:
    print("Computer wins!")

