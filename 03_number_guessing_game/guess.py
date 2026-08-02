import random

secret_number = random.randint(1,10)
while True:
    guess = int(input("Guess a number between 1 to 10:- "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        break

    elif guess > secret_number:
        print("Your guess was too high!")

    else:
        print("Your guess is too low!")