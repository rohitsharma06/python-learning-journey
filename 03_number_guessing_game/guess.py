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
            show_win_message(attempts)
            break

        elif guess > secret_number:
            print("Your guess was too high!")
            if attempts == max_attempts:
                show_game_over(secret_number)
                break

        else:
            print("Your guess is too low!")
            if attempts == max_attempts:
                show_game_over(secret_number)
                break

    play_again = input("Do you want to play again? (y/n): ")

    if play_again == "n":
        print("Thank you for playing!")
        break
