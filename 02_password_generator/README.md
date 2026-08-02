# Password Generator

A simple command-line password generator built using Python.

## Version 1 - Basic Password Generator

### Features
- User can choose the password length.
- Generates random passwords.
- Uses lowercase letters.
- Uses uppercase letters.
- Uses numbers.

### Concepts Learned
- `import`
- `random.choice()`
- Lists
- Combining lists
- `input()`
- Type casting
- `for` loop
- `range()`
- String building using `+=`

## Version 2 - Special Characters

### Features
- Added special characters.
- Password always contains at least one special character.

### Concepts Practiced
- List Combination
- `random.choice()`
- String Concatenation
- Loop Count (`range(num - 1)`)

## Version 3 - User Customization

### Features
- User can choose whether to include:
  - Uppercase letters
  - Numbers
  - Symbols
- Password is generated based on the selected options.
- Password length remains correct for all combinations.

### Concepts Practiced
- Conditional Statements (`if`)
- List Concatenation (`+=`)
- User Input (`input()`)
- Variables
- Program Logic

## Version 4 - Strong Password Generation

### Features
- Guarantees at least one lowercase letter.
- Guarantees at least one uppercase letter (if selected).
- Guarantees at least one number (if selected).
- Guarantees at least one symbol (if selected).
- Randomizes the character order using `random.shuffle()`.

### Concepts Practiced
- Lists
- append()
- len()
- random.shuffle()
- "".join()

## Version 5 - Input Validation

### Features
- Validates the minimum password length.
- Prevents users from entering an invalid password length.
- Keeps asking until valid input is entered.

### Concepts Practiced
- while loop
- Input Validation
- break
- f-string

## Version 6 - Generate Multiple Passwords

### Features
- Generate multiple passwords in one run.
- User can choose how many passwords to generate.
- Displays passwords with numbering.

### Concepts Practiced
- for loop
- range()
- Nested loops
- f-string