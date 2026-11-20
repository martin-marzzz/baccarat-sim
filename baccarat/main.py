"""
main.py 
Purpose: the main flow of the Baccarat simulator, it will gether the input from the user

Contains:
    - main flow of running Baccarat Simulation

Author: Martin Chan
Created: 2026-11-20
"""

from deck import Deck

deck = Deck(num_decks = 4)

print(deck.deal())
