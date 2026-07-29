# Calculator Project

A simple calculator project built step by step while learning Python.

---

# Version 1 - Addition

## Features
- Added user input.
- Performed addition of two numbers.
- Displayed the result.

## Concepts Learned
- print()
- input()
- Variables
- int()
- Basic Arithmetic

---

# Version 2 - Menu & Subtraction

## Features
- Added a simple menu.
- Added subtraction operation.
- Added choice selection using if and elif.

## Concepts Learned
- if
- elif
- Comparison Operators
- User Choice

---

# Version 3 - Multiplication & Division

## Features
- Added multiplication.
- Added division.
- Added Exit option.
- Added loop to run the calculator continuously.

## Concepts Learned
- while loop
- break
- Multiple Operations

---

# Version 4 - Code Refactoring

## Features
- Reduced repeated code.
- Asked for numbers only when a valid operation is selected.
- Improved code readability.

## Concepts Learned
- DRY (Don't Repeat Yourself)
- Code Refactoring
- Better Program Structure

---

# Version 5 - Functions

## Features
- Created separate functions for:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Menu Display
- Used `return` to send calculation results back.
- Replaced repeated calculation logic with reusable functions.

## Concepts Learned
- Functions (`def`)
- Function Calling
- Parameters
- Return Statement
- Code Reusability
---

# Version 6 - Exception Handling & Input Validation

## New Features
- Added exception handling using `try` and `except`.
- Prevented the calculator from crashing on invalid input.
- Created a reusable `get_number()` function.
- Used `ValueError` to catch invalid numeric input.
- Improved code reusability and readability.

## Concepts Learned
- `try`
- `except`
- `ValueError`
- Input Validation
- Reusable Functions

---

# Version 7 - Calculation History

## New Features
- Added calculation history using a list.
- Stored every calculation using `append()`.
- Added a new **History** menu option.
- Displayed history using a `for` loop.
- Handled empty history using `len()`.

## Concepts Learned
- Lists (`[]`)
- `append()`
- `for` loop with lists
- `len()`
- Data storage

## Version 8 - Code Refactoring with Dictionaries

### New Features
- Created an `operations` dictionary to store calculator functions.
- Created a `symbols` dictionary for operation symbols.
- Removed repeated code for Addition, Subtraction, Multiplication, and Division.
- Used a single block to handle all arithmetic operations.
- Added `continue` to safely handle division by zero.
- Made the calculator code cleaner and easier to maintain.

### Concepts Learned
- Dictionary (`dict`)
- Key-Value Pairs
- Functions as Dictionary Values
- Code Refactoring
- `continue` Statement
- Cleaner and Reusable Code

## Version 9 - File Handling

### New Features
- Saved every calculation to `history.txt`.
- Used Append Mode (`"a"`) to keep previous history.
- Displayed calculation history by reading from `history.txt`.
- Added exception handling to avoid crashes when the history file does not exist.
- Calculator history now remains available even after closing and reopening the program.

### Concepts Learned
- File Handling
- Write Mode (`"w"`)
- Append Mode (`"a"`)
- Read Mode (`"r"`)
- `open()`
- `write()`
- `read()`
- `close()`
- `FileNotFoundError`
- Persistent Data Storage