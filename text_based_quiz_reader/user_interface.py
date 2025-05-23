# Will copy and paste the code from the previous assignment here and make them into OOP structure

import os 
import sys
import time
from colorama import Fore, init

init(autoreset=True) # Initialize this code for colorama to reset the color after each print statement

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def return_to_main_menu():
    input("Press any key to return to the main menu...")   
    clear_screen()
    
def loading_screen():
    clear_screen()
    print(Fore.CYAN + "Loading...")
    bar_length = 30
    for i in range(1, bar_length + 1):
        time.sleep(0.1)
        bar = "=" * i
        progress = int((i / bar_length) * 100)
        sys.stdout.write(f"\r[{bar:<{bar_length}}] {progress}%")
        sys.stdout.flush()
    time.sleep(0.5)
    print("\n" + Fore.GREEN + "Ready!\n")
    time.sleep(1)
    clear_screen()