# This file will handle the user interface for the quiz creator.
# It will allow the user to create a quiz, read a quiz, or exit the program.
# This will be used by the main menu.

import os
from pathlib import Path
from colorama import Fore, Style
from quiz_logic import QuizCreator, Question

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

