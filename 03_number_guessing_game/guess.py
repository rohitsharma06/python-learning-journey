import random

def get_max_attempts(difficulty):
    if difficulty == 1:
        return 10

    elif difficulty == 2:
        return 7

    else:
        return 5

def show_win_message(attempts):
    print("Congratulations! You guessed correctly!")
    print(f"You guessed the number in {attempts} attempts.")

def show_game_over(secret_number):
    print("Game Over")
    print(f"The correct number was: {secret_number}")


def main():
    games_played = 0
    games_won = 0
    games_lost = 0

    while True:

        secret_number = random.randint(1,10)

        print("Select Difficulty:")
        print("1.Easy \n2.Medium \n3.Hard")

        try:
            difficulty = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter number choice only")
            continue

        if difficulty < 1 or difficulty > 3:
            print("Please enter 1, 2, or 3 only.")
            continue

        attempts = 0

        max_attempts = get_max_attempts(difficulty)

        while True:
            try:
                guess = int(input("Guess a number between 1 to 10:- "))
            except ValueError:
                print("Please Enter numbers only")
                continue

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            attempts += 1
            print(f"Attempt Left: {max_attempts - attempts}")
            if guess == secret_number:
                games_won += 1
                show_win_message(attempts)
                break

            elif guess > secret_number:
                print("Your guess was too high!")
                if attempts == max_attempts:
                    games_lost += 1
                    show_game_over(secret_number)
                    break

            else:
                print("Your guess is too low!")
                if attempts == max_attempts:
                    games_lost += 1
                    show_game_over(secret_number)
                    break

        games_played += 1
        play_again = input("Do you want to play again? (y/n): ")

        if play_again == "n":

            print("\n========== Game Statistics ==========")
            print(f"Games Played : {games_played}")
            print(f"Games Won    : {games_won}")
            print(f"Games Lost   : {games_lost}")
            print("=====================================")

            print("Thank you for playing!")
            break
main()