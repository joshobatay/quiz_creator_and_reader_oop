# This will be the main menu for the quiz creator
# It will allow the user to create a quiz, read a quiz, or exit the program

from user_interface import clear_screen, developer_info, create_quiz

def main_menu():
    while True:
        from pyfiglet import figlet_format
        from colorama import Fore, Style, init
        
        clear_screen()
        text = figlet_format(text="Welcome to the Quiz Creator!", font="ansi_regular", width=150)
        print(Fore.CYAN + text)
        
        print("""
1. Create your own quiz
2. Meet the developer
3. Exit the program
        """)
        
        user_choice = input("Enter your choice: ").strip().lower()
        
        if user_choice in ["1", "one", "create your own quiz"]:
            create_quiz()
        elif user_choice in ["2", "two", "meet the developer"]:
            developer_info()
        elif user_choice in ["3", "three", "exit the program"]:
            clear_screen()
            print("Exiting the program...")
            break
        else:
            clear_screen()
            print(Fore.RED + "Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main_menu()
