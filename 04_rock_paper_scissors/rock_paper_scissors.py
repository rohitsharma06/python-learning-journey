import random

choices = ["rock", "paper", "scissors"]

games_played = 0
player_wins = 0
computer_wins = 0
ties = 0
while True:

    print("====== Rock Paper Scissors ======")

    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = int(input("Enter your choice: "))

    player_choice = choices[choice-1]
    print(f"Player Choice : {player_choice}")

    computer_choice = random.choice(choices)
    print(f"Computer Choice : {computer_choice}")


    if player_choice == computer_choice:
        ties += 1
        print("It's a tie")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        player_wins += 1
        print("You win!")

    else:
        computer_wins += 1
        print("Computer wins!")

    games_played += 1

    play_again = input("Do you want to play again? (y/n): ")

    if play_again == "n":
        break

print("\n========== Statistics ==========")
print(f"Games Played : {games_played}")
print(f"You Won      : {player_wins}")
print(f"Computer Won : {computer_wins}")
print(f"Tie Games    : {ties}")
print("================================")



