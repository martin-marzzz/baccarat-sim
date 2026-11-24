"""
main.py 
Purpose: the main flow of the Baccarat simulator, it will gether the input from the user

Contains:
    - main flow of running Baccarat Simulation

Author: Martin Chan
Created: 2026-11-20
"""

import sys

import rules
from deck import Deck

def main():
    # User have to pass in an argument
    if len(sys.argv) > 1:
        try:
            num_decks = int(sys.argv[1])
        except ValueError:
            print("Please enter a valid number.")
            return
    
    if not rules.is_valid_num_decks(num_decks):
        print("Number of decks must within 4 and 8.")
        return

    deck = Deck(num_decks = num_decks)
    #print(f"Created deck with {len(deck.cards)} cards")

    player_total = 0
    banker_total = 0
    
    player_first = deck.deal()
    banker_first = deck.deal()
    player_second = deck.deal()
    banker_second = deck.deal()


    player_total = int(player_first.value + player_second.value)
    banker_total = int(banker_first.value + banker_second.value)
    
    print(f"Player's hand {player_first.rank}{player_first.suit}, {player_second.rank}{player_second.suit}")
    print(f"Player total after first round is {rules.get_unit_digit(player_total)}")
    print(f"Banker's hand {banker_first.rank}{banker_first.suit}, {banker_second.rank}{banker_second.suit}")
    print(f"Bankyer total after first round is {rules.get_unit_digit(banker_total)}")


if __name__ == "__main__":
    main()
