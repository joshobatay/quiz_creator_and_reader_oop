''' Will copy paste the code from the previous assignment here 
that is related to the function of the main menu and make them into OOP structure '''

import pyfiglet
from colorama import Fore, init
from quiz_logic import QuizReader, DeveloperInfo

init(autoreset=True)  # Initialize this code for colorama to reset the color after each print statement

def main_menu():
    while True:
        text = "Welcome to the Quiz Reader!"
        print(Fore.YELLOW + pyfiglet.figlet_format(text, font="ansi_regular", width=100))
        print('''
1. Read a quiz file
2. Meet the developer
3. Exit the program
''')
        
        choice = input("Enter your choice: ")
        if choice == "1":
            QuizReader().file_finder()
        elif choice == "2":
            DeveloperInfo().show_developer_info()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main_menu()
            
            