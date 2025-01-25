# quiz.py

questions = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin", "Rome"], "correct": 0},
    {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Saturn", "Jupiter", "Uranus"], "correct": 2},
    # Add more questions here...
]

def quiz_game():
    score = 0
    for question in questions:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i + 1}. {answer}")
        user_answer = int(input("Enter your answer: ")) - 1
        if user_answer == question["correct"]:
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is {question['answers'][question['correct']]}")
    print(f"\nYour final score is {score} out of {len(questions)}")

def main():
    print("Welcome to the quiz game!")
    quiz_game()

if __name__ == "__main__":
    main()
