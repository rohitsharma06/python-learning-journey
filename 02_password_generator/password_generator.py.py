import random


lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

uppercase = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*","(",")","/","-","|"]

include_uppercase = input("Include Uppercase? (y/n):")
include_numbers   = input("Include Numbers? (y/n):")
include_symbols   = input("Include Symbols? (y/n):")

character = lowercase

if include_uppercase == "y":
    character += uppercase

if include_numbers == "y":
    character += numbers

if include_symbols == "y":
    character += symbols

minimum_length = 1
if include_uppercase == "y":
    minimum_length += 1

if include_numbers == "y":
    minimum_length += 1

if include_symbols == "y":
    minimum_length += 1

while True:
    num = int(input("Enter the number of characters: "))

    if num >= minimum_length:
        break
    print(f"Password length should be at least {minimum_length}.")

password_count = int(input("How many passwords do you want to generate? "))

for i in range(password_count):

    password = []

    password.append(random.choice(lowercase))

    if include_uppercase == "y":
        password.append(random.choice(uppercase))

    if include_numbers == "y":
        password.append(random.choice(numbers))

    if include_symbols == "y":
        password.append(random.choice(symbols))

    remaining_characters = num - len(password)

    for _ in range(remaining_characters):
        password.append(random.choice(character))

    random.shuffle(password)
    password = "".join(password)

    print(f"{i + 1}. {password}")