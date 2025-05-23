# Will copy paste the code from the previous assignment here and make them into OOP structure
# Carefully check the code and make sure that the code is correct and does not have any errors
# Only splitted the code and put them into here that is related to the quiz logic

import json
import tkinter as tk
from tkinter import filedialog
from colorama import Fore
from user_interface import clear_screen, loading_screen, return_to_main_menu

class DifficultyManager:
    def select_diffculty(self):
        clear_screen()
        print(f'''
Select Difficulty Level:
{Fore.GREEN}1. Easy (10 lives)
{Fore.YELLOW}2. Normal (5 lives)
{Fore.RED}3. Hard (3 lives)
{Fore.MAGENTA}4. Impossible (1 life)
''')
        
        choice = input("Enter your choice (1 - 4): ")
        clear_screen()
        return {"1": 10, "2": 5, "3": 3, "4": 1}.get(choice, 10)  # Default to Normal (5 lives) if invalid input
    
class QuizReader(DifficultyManager):
    def file_finder(self):
        clear_screen()
        temp_root = tk.Tk()
        temp_root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Select a quiz file",
            filetypes=[("JSON files", "*.json")]
        )
        temp_root.destroy()
        
        if not file_path:
            print("No File Selected. Returning to main menu...")
            return
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                quiz_name = data["quiz_name"]
                questions = data["questions"]
                
                print(f"Welcome to the quiz: {quiz_name}\n")
                lives = self.select_diffculty()
                loading_screen()
                score = 0
                
                for key, q in questions.items():
                    print(f"\n{Fore.YELLOW}{key.replace('_', ' ').title()}: {q['Question']}")
                    for option, answer in q["Choices"].items():
                        print(f"{option}: {answer}")
                        
                    while True:
                        answer = input("Enter your answer (A/B/C/D): ").strip().lower()
                        if answer == q["Correct Answer"]:
                            score += 1
                            print(Fore.GREEN + "Correct!")
                            break
                        elif answer not in "ABCD":
                            print(Fore.RED + "Invalid choice. Please enter A, B, C, or D.")
                        else:
                            lives -= 1
                            print(Fore.RED + f"Wrong! The correct answer was {q['Correct Answer']}.")
                            print(Fore.YELLOW + f"Lives left: {lives}")
                            break
                    print(f"Explanation: {q['Explanation']}\n")
                    input("Press Enter to continue...")
                    clear_screen()
                    
                    if lives <= 0:
                        print(Fore.YELLOW + f"Score: {score}/{len(questions)}")
                        print(Fore.RED + "Game Over!")
                        return_to_main_menu()
                        return
                    
                print(Fore.YELLOW + "Congratulations! " +
                      Fore.GREEN + f"You completed the quiz with a score of {score}/{len(questions)}!")
                return_to_main_menu() 
                
        except Exception as e:
            print(f"Error reading the file: {e}")
            
class DeveloperInfo(DifficultyManager):
    def show_developer_info(self):
        clear_screen()
        print(Fore.MAGENTA + "Developer: BSCpE 1-6 | Gabriel Josh A. Obatay")
        print(Fore.GREEN + "Email: joshobatay2005@gmail.com")
        return_to_main_menu() 