questions = [
    { "question": "What is the capital of India?",
      "options":["Mumbai", "Delhi", "Kolkata", "Chennai"],
      "answer": "Delhi"
      },

    {
        "question": "Which language are we learning?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "func", "create"],
        "answer": "def"
    }
]


score = 0
for question in questions:
    print(question["question"])

    for i in range(len(question["options"])):
        print(f"{i + 1}. {question['options'][i]}")

    try:
        answer = int(input("Enter your answer (1-4): "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if answer < 1 or answer > len(question["options"]):
        print("Please choose a valid option.")
        continue

    selected_answer = question["options"][answer - 1]

    print(f"You selected: {selected_answer}")

    if selected_answer.lower() == question["answer"].lower():
        print("Provided Answer is correct")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}.")



    print()

percentage = (score / len(questions)) * 100

print("========== QUIZ RESULT ==========")
print(f"Your Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")
print("==================================")

if percentage >= 80:
    print("     Excellent!")
elif percentage >= 50:
    print("     Good job!")
else:
    print("     Keep practicing!")

print("==================================")