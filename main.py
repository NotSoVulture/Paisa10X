import random
import os
from style import Style

STARTING_MONEY = 50

N = "\n" # Newline
ARROW = f"{Style.BLUE}>>{Style.RESET}"
DOT = f"{Style.YELLOW}•{Style.RESET}"

def clear():
    os.system('cls')  # Windows Exclusive

def home():
    clear()
    print(f"{Style.MAGENTA}{N}+-- HOME --+{Style.RESET}")
    print(f"| 1. Play  |")
    print(f"| 2. Quit  |")
    print(f"{Style.MAGENTA}+----------+{Style.RESET}")
    choice = input(f"{N}{ARROW} ").strip()
    return choice

def get_bet(money):
    while True:
        bet_input = input(f"{N}{DOT} Enter bet or [Q] {ARROW} ").strip()
        if bet_input.lower() == 'q':
            return None
        try:
            bet = int(bet_input)
            if 1 <= bet <= money:
                return bet
            else:
                print(f"{Style.RED}{N}Error{Style.RESET}: Bet must be between $1 and your current money.")
        except ValueError:
            print(f"{Style.RED}{N}Error{Style.RESET}: Enter a Valid Bet!")

class CardGame:
    def __init__(self):
        self.money = STARTING_MONEY
        self.playername = ""

    def play(self):
        clear()
        self.playername = input(F"{N}{DOT} Player Name {ARROW} ").strip().title()
        clear()
        print(f"{N}Welcome, {Style.MAGENTA}{self.playername}{Style.RESET}! You currently have {Style.GREEN}${self.money}{Style.RESET}.")

        while self.money > 0:
            bet = get_bet(self.money)
            if bet is None:
                print(f"{N}You're leaving with {Style.RED}${self.money}{Style.RESET}.")
                break

            player_card = random.randint(1, 12)
            cpu_card = random.randint(1, 12)
            print(f"{N}{Style.MAGENTA}+----------+{Style.RESET}")
            print(f"|{Style.YELLOW} YOU  {Style.RESET} {Style.GREEN}{player_card:2d}{Style.RESET} |")
            print(f"|{Style.YELLOW} CPU  {Style.RESET} {Style.RED}{cpu_card:2d}{Style.RESET} |")
            print(f"{Style.MAGENTA}+----------+{Style.RESET}")

            if player_card == cpu_card:
                print(f"{N}{Style.YELLOW}It's a DRAW! {Style.RESET}")
            elif player_card > cpu_card:
                if random.random() < 0.05:
                    win_amount = bet * 10
                    print(f"{N}{Style.GREEN}{Style.BOLD}JACKPOT! You won ${win_amount}! {Style.RESET}")
                else:
                    multiplier = random.randint(1, 2)
                    win_amount = multiplier * bet
                    print(f"{N}{Style.GREEN}You won ${win_amount}! {Style.RESET}")
                self.money += win_amount
            else:
                print(f"{N}{Style.RED}You lost ${bet}. {Style.RESET}")
                self.money -= bet

            if self.money <= 0:
                print(f"{N}{Style.RED}You're out of money! {Style.RESET}")
            else:
                print(f"You now have {Style.CYAN}${self.money}{Style.RESET}.")

if __name__ == "__main__":
    while True:
        choice = home()
        if choice == '1':
            game = CardGame()
            game.play()
            input(f"{N}Press {Style.BLACK}Enter{Style.RESET} to return to Home Screen... ")
        elif choice == '2':
            print(f"{N}{Style.MAGENTA}Goodbye! {Style.RESET}")
            break
        else:
            print(f"{N}{Style.RED}Invalid choice. Please select 1 or 2. {Style.RESET}")
            input(f"Press {Style.BLACK}Enter{Style.RESET} to continue... ")