import random

def intro():
    i = "\nWelcome to the Game!"
    print(i)

def game_over():
    i = "Game Over!\n"
    print(i)

def main():
    intro()

    playername = input("• Player Name >> ").strip().title()
    money = 50
    print(f"\nWelcome, {playername}! You currently have ${money}.")

    play = True
    while play:
        bet = int(input("• Place your bet >> "))
        invalid_bet = bet > money or bet < 1

        while invalid_bet:
            print("\nError: Enter a Valid Bet!")
            bet = int(input("• Place your bet >> "))
            invalid_bet = bet > money or bet < 1
        
        player_card = random.randint(1, 12)
        cpu_card = random.randint(1, 12)

        print(f"\n~ Your Card: {player_card}\n~ CPU Card: {cpu_card}")

        if player_card == cpu_card:
            print("\nIt's a DRAW!")
        elif player_card > cpu_card:
            multiplier = random.randint(1, 2)
            print(f"\nYou won ${multiplier * bet}.")
            money += (multiplier * bet)
        else:
            print(f"\nYou lost ${bet}.")
            money -= bet
        
        if money <= 0:
            print("You're out of money!")
            game_over()
            play = False
        else:
            print(f"You now have ${money}.")
            ask = input("\nDo you want to keep playing? (Y/N) >> ")
            if ask.strip().capitalize() == "Y":
                play = True
            else:
                print(f"You're leaving with ${money}.")
                game_over()
                play = False
main()