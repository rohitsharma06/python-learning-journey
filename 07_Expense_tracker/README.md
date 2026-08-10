# Expense Tracker

A beginner-friendly Python Expense Tracker built to practice core Python concepts through a real-world project.

## Features

* View all expenses
* Add a new expense
* Delete an expense using Expense ID
* Calculate total expenses
* View expenses by category
* Automatically save expenses to a file
* Automatically load saved expenses when the program starts
* Automatically record the current date
* Input validation for amounts and menu choices
* Prevent empty descriptions and categories

## Concepts Practiced

This project helped me practice:

* Variables
* Lists
* Dictionaries
* `if / elif / else`
* `for` loops
* `while` loops
* Functions
* Function arguments
* `return`
* `try / except`
* `ValueError`
* String methods
* `.strip()`
* `.title()`
* `datetime`
* File handling
* Reading and writing files
* `FileNotFoundError`
* Dictionary operations
* `append()`
* `remove()`
* `split()`
* f-strings
* Number formatting
* Data persistence
* Unique ID generation

## Project Structure

```text
07_expense_tracker/
│
├── expense_tracker.py
├── expenses.txt
└── README.md
```

## How It Works

When an expense is added, the program stores:

* Expense ID
* Amount
* Description
* Category
* Date

Example:

```text
Expense ID: 1
Amount    : ₹500.00
Details   : Groceries
Category  : Food
Date      : 10-08-2026
```

The expenses are stored in `expenses.txt`, so the data remains available even after closing and reopening the program.

## Menu

```text
========== EXPENSE TRACKER ==========
1. View Expenses
2. Add Expense
3. Delete Expense
4. Total Expenses
5. Category Summary
6. Exit
=====================================
```

## What I Learned

The main goal of this project was to understand how different Python concepts work together to build a complete command-line application.

I also practiced handling user input, validating data, working with functions, and storing data permanently using files.

## How to Run

Make sure Python is installed, then run:

```bash
python expense_tracker.py
```

## Project Status

**Completed ✅**

This project is part of my Python learning journey, where I am building projects step-by-step to strengthen my Python fundamentals.
