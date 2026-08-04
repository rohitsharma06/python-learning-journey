import random

choices = ["rock", "paper", "scissors"]

games_played = 0
player_wins = 0
computer_wins = 0
ties = 0

def get_player_choice(choices):
    choice = int(input("Enter your choice: "))
    player_choice = choices[choice-1]
    return player_choice

def get_computer_choice(choices):
    return random.choice(choices)

def show_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie")
        return "tie"

    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        return "player"

    else:
        print("Computer wins!")
        return "computer"

def show_statistics(games_played, player_wins, computer_wins, ties):
    print("\n========== Statistics ==========")
    print(f"Games Played : {games_played}")
    print(f"You Won      : {player_wins}")
    print(f"Computer Won : {computer_wins}")
    print(f"Tie Games    : {ties}")
    print("================================")

while True:

    print("====== Rock Paper Scissors ======")

    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player_choice = get_player_choice(choices)
    print(f"Player Choice : {player_choice}")

    computer_choice = get_computer_choice(choices)
    print(f"Computer Choice : {computer_choice}")


    result = show_result(player_choice, computer_choice)

    if result == "player":
        player_wins += 1

    elif result == "computer":
        computer_wins += 1

    else:
        ties += 1

    games_played += 1

    play_again = input("Do you want to play again? (y/n): ")

    if play_again == "n":
        break

show_statistics(games_played, player_wins, computer_wins, ties)




