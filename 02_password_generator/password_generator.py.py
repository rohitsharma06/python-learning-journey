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

num = int(input("Enter the number of characters: "))


# if include_symbols == "y":
#     password = random.choice(symbols)
#     loop_count = num -1
# else:
#     password = ""
#     loop_count = num
#
# for _ in range(num - 1):
#     password += random.choice(character)
#
# print(password)


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

print(password)