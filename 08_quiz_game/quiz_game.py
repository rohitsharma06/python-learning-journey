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
    for option in question["options"]:
        print(option)

    answer = input("Enter your answer: ")
    if answer == question["answer"]:
        print("Provided Answer is correct")
        score += 1
    else:
        print("Provided answer is wrong")



    print()

print("========== QUIZ RESULT ==========")
print(f"Your Score: {score}/{len(questions)}")
print("==================================")