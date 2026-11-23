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
    print(f"Created deck with {len(deck.cards)} cards")

if __name__ == "__main__":
    main()
