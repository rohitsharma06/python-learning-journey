import random

while True:

    secret_number = random.randint(1,10)

    print("Select Difficulty:")
    print("1.Easy \n2.Medium \n3.Hard")

    difficulty = int(input("Enter your choice: "))

    attempts = 0

    if difficulty == 1:
        max_attempt =10
    elif difficulty == 2:
        max_attempt = 7
    else:
        max_attempt = 5

    while True:
        guess = int(input("Guess a number between 1 to 10:- "))

        attempt += 1
        print(f"Attempt Left: {max_attempt - attempts}")
        if guess == secret_number:
            print("Congratulations! You guessed correctly!")
            print(f"You guessed The number in {attempts} attempts.")
            break

        elif guess > secret_number:
            print("Your guess was too high!")
            if attempts == max_attempt:
                print("Game Over")
                print(f"The correct number was: {secret_number}")
                break

        else:
            print("Your guess is too low!")
            if attempts == max_attempt:
                print("Game Over")
                print(f"The correct number was: {secret_number}")
                break

    play_again = input("Do you want to play again? (y/n): ")

    if play_again == "n":
        print("Thank you for playing!")
        break
