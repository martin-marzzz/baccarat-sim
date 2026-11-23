"""
ruels.py 
Purpose: def functions to determine who win the bet.
    There would be rules for counting who is the winning.
    Also the function control the order of dealing.

Contains:
    - [functions]

Reference: The rule book from Crown Perth Baccarat
    https://www.crownperth.com.au/getmedia/f2d3d3cd-9930-4ca5-8a00-30feb12e7f75/crown-perth-gaming-mini-baccarat-and-baccarat-rules.pdf

Author: Martin Chan
Created: 2026-11-20`
"""

from typing import Optional

def is_valid_num_decks(num_deck: int) -> bool:
    """Return True if the number of decks is 4-8."""
    return 4 <= num_deck <= 8

def banker_player_first_hand(card_in_hand: int) -> bool:
    """Return True if either one have enough for the first hand."""
    return card_in_hand < 2

def is_total_less_than_six(total: int) -> bool:
    """Return True if total is 0-5."""
    return total <= 5

def player_should_draws(player_total: int) -> bool:
    """Return True if play's hand is 0-5, player will draw. Greater will not draw."""
    return is_total_less_than_six(player_total)

def banker_should_draws(banker_total: int, player_third: Optional[int]) -> bool:
    """
    Return True if banker must draw a third card.

    player_third: the third card player drawn on (0-9).
    """

    # Case 1: Player stood (no third card)
    if player_third is None:
        return banker_total <= 5

    # Case 2: Player drew a third card
    if banker_total <= 2:
        return True
    if banker_total == 3:
        return player_third != 8
    if banker_total == 4:
        return player_third in (2, 3, 4, 5, 6, 7)
    if banker_total == 5:
        return player_third in (4, 5, 6, 7)
    if banker_total == 6:
        return player_third in (6, 7)
    
    # Banker total is 7
    return False

def get_unit_digit(total: int) -> int:
    return total % 10

def win_on_six(banker_total: int) -> bool:
    return banker_total == 6

def get_winner(banker_total: int, player_total: int) -> str:
    if banker_total > player_total:
        return "Banker"
    
    elif player_total > banker_total:
        return "Player"
    
    return "Tie" 

def get_odds(banker_total: int, player_total: int) -> float:
    if banker_total > player_total:
        if win_on_six(banker_total):
            return 1.5
        else:
            return 2

    elif player_total > banker_total:
        return 2

    else:
        return 1
