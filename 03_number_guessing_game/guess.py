import random

secret_number = random.randint(1,10)

attempt = 0

while True:
    guess = int(input("Guess a number between 1 to 10:- "))

    attempt += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        print(f"You guessed The number in {attempt} attempts.")
        break

    elif guess > secret_number:
        print("Your guess was too high!")

    else:
        print("Your guess is too low!")