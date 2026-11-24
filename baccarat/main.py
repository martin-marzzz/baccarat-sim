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
    num_deck = 8
    if len(sys.argv) > 1:
        try:
            num_decks = int(sys.argv[1])
        except ValueError:
            print("Please enter a valid number.")
            return
    
    if not rules.is_valid_num_decks(num_decks):
        print("Number of decks must within 4 and 8.")
        return

    result = []
    round_played = 0
    player_win = 0
    banker_win = 0
    tie_win = 0

    deck = Deck(num_decks = num_decks)

    while deck.count() > 20:
        round_played += 1

        p1 = deck.deal()
        b1 = deck.deal()
        p2 = deck.deal()
        b2 = deck.deal()
        p3 = None
        b3 = None

        player_total = (p1.value + p2.value) % 10
        banker_total = (b1.value + b2.value) % 10

        print(f"Initial → Player: {player_total}, Banker: {banker_total}")

        if player_total >= 8 or banker_total >= 8:
            print(f"Final   → Player: {player_total}, Banker: {banker_total} (Natural)")
            print(f"Winner: {rules.get_winner(player_total, banker_total)}")
            print("-" * 30)
            if rules.get_winner(player_total, banker_total) == "Player":
                player_win += 1
            elif rules.get_winner(player_total, banker_total) == "Banker":
                banker_win += 1
            else:
                tie_win += 1
            continue

        # Player third card
        if rules.player_should_draw(player_total):
            p3 = deck.deal()
            player_total = (player_total + p3.value) % 10

        # Banker third card
        player_third_value = p3.value if p3 else None
        if rules.banker_should_draw(banker_total, player_third_value):
            b3 = deck.deal()
            banker_total = (banker_total + b3.value) % 10
        
        if rules.get_winner(player_total, banker_total) == "Player":
            player_win += 1
        elif rules.get_winner(player_total, banker_total) == "Banker":
            banker_win += 1
        else:
            tie_win += 1


        print(f"Final   → Player: {player_total}, Banker: {banker_total}")
        print(f"Winner: {rules.get_winner(player_total, banker_total)}")
        print("-" * 30)
    
    print("=" * 30)
    print(f"Round Played: {round_played}")
    print(f"Player win: {player_win}")
    print(f"Banker win: {banker_win}")
    print(f"Tie win: {tie_win}")

if __name__ == "__main__":
    main()
