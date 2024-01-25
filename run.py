
import colorama
import time
from colorama import Fore, Back, Style

# introduction
print(f"{Fore.GREEN}\nWelcome to the Python Quiz Game!\n{Fore.WHITE}")
print(f"{Fore.BLUE}Please select the correct answer. For each question "
      f"answered correctly within 15 seconds, you will earn 10 points. "
      f"If it takes longer than that, you earn 5 points:{Fore.WHITE}\n\n")


# define a function.
def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])

        for option in question["options"]:
            print(option)
        # Start the timer
        start_time = time.time()
        try:
            answer = input(f"{Fore.BLUE}Your answer: ")
            # End the timer
            end_time = time.time()
            # Calculate elapsed time
            elapsed_time = end_time - start_time
            if int(answer) == question["answer"]:
                # If the participant answers within 15 seconds
                if elapsed_time <= 15:
                    print(f"{Fore.GREEN}Correct! 10 points{Fore.WHITE}")
                    score += 10
                else:
                    print(f"{Fore.GREEN}Correct! 5 points{Fore.WHITE}")
                    score += 5
            else:
                print(f"{Fore.RED}Incorrect!{Fore.WHITE}")
            if str or int(len(value)) != 1:
                raise ValueError(
                    f" 1 number digit is required not {len(value)}"
                    )
        except ValueError as e:
            print(f"{Fore.RED} {e}, please put a valid number.{Fore.WHITE}")

    # This print statement ends the quiz and shows the final score.
    print(f"{Fore.YELLOW}Goodbye, you have Completed the Quiz!{Fore.WHITE}")
    print(f"{Fore.BLUE}Your score: {score}{Fore.GREEN} \
        out of {len(questions) * 10}{Fore.WHITE}")


# Example questions (this would be provided in the rest of your script)

questions = [
    {
        "question":
        "Which of the following is not a primitive data type in Python?",
        "options": ["1) Integer", "2) String", "3) List", "4) Function"],
        "answer": 4
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["1) Jupiter", "2) Mars", "3) Earth"],
        "answer": 1
    },
    {
        "question": "What is the result of the following code snippet?",
        "code": ["x = 7", "print(x * 3)"],
        "options": ["1) 8", "2) error", "3) 15", "4) 21"],
        "answer": 4
    },
    {
        "question":
        "Which programming language is known as the 'language of the web'?",
        "options": ["1) Python", "2) Java", "3) JavaScript"],
        "answer": 3
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1) define", "2) func", "3) def", "4) function"],
        "answer": 3
    },
    {
        "question":
        "What does the 'self' parameter refer to in a class method in Python?",
        "options": [
            "1) It refers to the current object instance",
            "2) It refers to the parent class",
            "3) It refers to the derived class",
            "4) It refers to the static class"
        ],
        "answer":
        1
    },
    {
        "question":
        "Which module in Python is used for working with regular expressions?",
        "options": ["1) datetime", "2) math", "3) os", "4) re"],
        "answer": 4
    },
    {
        "question": "How do you comment a line of code in Python?",
        "options":
        ["1) // comment", "2) /* comment */", "3) # comment", "4) n"],
        "answer": 3
    },
]

# Run the quiz
quiz(questions)
