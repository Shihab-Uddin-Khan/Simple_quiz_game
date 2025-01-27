mcqs = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["A. Chittagong", "B. Dhaka", "C. Khulna", "D. Sylhet"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known for AI and ML?",
        "options": ["A. Java", "B. C++", "C. Python", "D. JavaScript"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "C"
    }  
]


def interface():
    print("\nSIMPLE_QUIZ_GAME")
    print("1. Start the game")
    print("2. Instructions")
    print("3. Exit")


def main_operation(value):
    if value == 1:
        score = 0
        for index, mcq in enumerate(mcqs, start=1):
            print(f"\nQ{index}: {mcq['question']}\n")
            for option in mcq['options']:
                print(option)
            user_answer = input("Enter answer (A/B/C/D or 'exit' to quit): ").strip().upper()
            if user_answer == "EXIT":
                print("You exited the quiz!")
                break
            if user_answer == mcq['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {mcq['answer']}")
        print(f"\nYour final score is: {score}")
    elif value == 2:
        print("\nWelcome to the Quiz Game!")
        print("Here are the rules and instructions you need to follow:\n")
        print("1. The quiz consists of multiple-choice questions (MCQs).")
        print("2. Each question will have four options: A, B, C, and D.")
        print("3. You must type the correct option letter (A, B, C, or D) and press Enter.")
        print("4. Each correct answer will earn you 1 point.")
        print("5. No points will be deducted for wrong answers.")
        print("6. Try to answer all the questions to get the best score.")
        print("7. Type 'exit' anytime to quit the quiz.\n")
        print("Best of luck!\n")
        a = int(input("Enter 1 to go back to the menu: "))
        if a == 1:
            interface()
            value = int(input("Enter your choice: "))
            main_operation(value)
        else:
            print("Wrong input. Returning to menu...")
            interface()
    else:
        print("Have a good day!")


interface()
value = int(input("Enter your choice: "))
main_operation(value)
