"""
test_rules.py 
Purpose: Test file for the rules functions.
Run with: python -m pytest test_rules.py -v

Contains:
    - testing function, if the result is correct than okay.

Author: Martin Chan
Created: 2026-11-21
"""

from baccarat.rules import (
    is_valid_num_decks,
    banker_player_first_hand,
    is_total_less_than_six,
    player_should_draws,
    banker_should_draws,
    win_on_six,
    get_winner,
    get_odds
)

def test_is_valid_num_decks():
    #Test outside the range
    assert is_valid_num_decks(0) is False 
    assert is_valid_num_decks(9) is False

    #Test inside the range
    assert is_valid_num_decks(4) is True
    assert is_valid_num_decks(5) is True 
    assert is_valid_num_decks(8) is True

def test_banker_player_first_hand():
    #Test the hand is less than 2, which is less number of card for the first 
    assert banker_player_first_hand(0) is True 
    assert banker_player_first_hand(1) is True 

    #Test the hand is enough which return False
    assert banker_player_first_hand(2) is False 

def test_is_total_less_than_six():
    #Test the total is less than six then draw card
    assert is_total_less_than_six(0) is True
    assert is_total_less_than_six(5) is True

    #Test the total is greter than 5, return False
    assert is_total_less_than_six(6) is False
    assert is_total_less_than_six(9) is False

def test_player_should_draws():
    #Test the player will draw card if hand less than 6
    assert player_should_draws(0) is True
    assert player_should_draws(5) is True

    #Test the player hand is greater then 6 in first -> False
    assert player_should_draws(6) is False
    assert player_should_draws(9) is False

def test_banker_should_draws():
    #Test the banker hand diff total and player has no third card
    assert banker_should_draws(0, None) is True
    assert banker_should_draws(6, None) is False

    #Test the bank hand diff total and ploayer draw the thid card
    assert banker_should_draws(2, 5) is True  
    assert banker_should_draws(3, 7) is True
    assert banker_should_draws(3, 8) is False  
    assert banker_should_draws(4, 2) is True  
    assert banker_should_draws(5, 6) is True

    #Test cases rather than above
    assert banker_should_draws(7, 6) is False 
    assert banker_should_draws(8, 7) is False 
    assert banker_should_draws(9, 8) is False 

def test_win_on_six():
    #Test the banker total is 6
    assert win_on_six(6) is True
    assert win_on_six(2) is False
    assert win_on_six(7) is False

def test_get_winner():
    #Test who is the winner or tie -> str
    assert get_winner(1, 1) is "Tie"

    #Test banker win
    assert get_winner(5, 4) is "Banker"

    #Test player win
    assert get_winner(7, 8) is "Player"

def test_get_odds():
    #Test the odds return as 1.5 or 2 
    assert get_odds(5, 4) == 2.0
    assert get_odds(7, 8) == 2.0

    #Test the odds is 1.5 when banker win on total 6
    assert get_odds(6, 5) == 1.5
    
    #Test on the tie
    assert get_odds(5, 5) == 1.0


if __name__ == "__main__":
    test_is_valid_num_decks()
    test_banker_player_first_hand()
    test_is_total_less_than_six()
    test_player_should_draws()
    test_player_should_draws()
    test_banker_should_draws()
    test_win_on_six()
    test_get_winner()
    test_get_odds()
