# This file will handle the user interface for the quiz creator.
# It will allow the user to create a quiz, read a quiz, or exit the program.
# This will be used by the main menu.

import os
from pathlib import Path
from colorama import Fore, Style, init
from quiz_logic import QuizCreator, Question

init(autoreset=True)  # Initialize colorama to reset colors automatically

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def developer_info():
     while True:
        clear_screen()
        print(Fore.GREEN + """
Program made by: BSCpE 1-6 | Gabriel Josh A. Obatay
        """ + Style.RESET_ALL)
        choice = input("Press 'b' to go back to the main menu: ").strip().lower()
        if choice == "b":
            clear_screen()
            break

def create_quiz():
    clear_screen()
    quiz_name = input(Fore.YELLOW + "Enter the name of the quiz: ").strip()
    quiz = QuizCreator(quiz_name)
    question_count = 1
    
    while True:
        question = input(Fore.YELLOW + f"Enter question {question_count}: ").strip()
        print(Fore.YELLOW + "Enter the Choices:")
        choices = {
            "A": input("A: ").strip(),
            "B": input("B: ").strip(),
            "C": input("C: ").strip(),
            "D": input("D: ").strip()
        }
        
        while True:
            correct_answer = input(Fore.YELLOW + "Enter the correct answer (A|B|C|D): ").strip().upper()
            if correct_answer in ["A", "B", "C", "D"]:
                break
            else:
                print(Fore.RED + "Invalid choice. Please enter A, B, C, or D.")

        explanation = input(Fore.YELLOW + "Enter the explanation: ").strip()

        question_object = Question(question, choices, correct_answer, explanation)
        quiz.add_question(question_object)

        clear_screen()
        print(f"Quiz name: {Fore.GREEN + quiz_name}")
        print(f"Added Question: {Fore.GREEN + question}")
        for key, choice_text in choices.items():
            print(f"{key}: {Fore.GREEN + choice_text}")
        print(f"Correct Answer: {Fore.GREEN + correct_answer}")
        print(f"Explanation: {Fore.GREEN + explanation}")

        user_input = input(f"Do you want to add another question? (Type {Fore.RED + 'stop'} to quit or press Enter to continue): ").strip().lower()
        if user_input == "stop":
            clear_screen()
            break

        question_count += 1
        clear_screen()

    if quiz.questions:
        desktop_path = Path.home() / "Desktop"
        destination = desktop_path / "create_your_own_quiz.json"

        if destination.exists():
            overwrite = input(f"The file already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
            clear_screen()
            if overwrite != "yes":
                print(Fore.MAGENTA + "File not overwritten.")
                return

        try:
            quiz.save_to_json(destination)
            print(Fore.GREEN + "JSON file created successfully.")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
