"""
deck.py 
Purpose: Representing the deck behavior like in real world and deck management for Baccarat.
    Input: Number of decks
    Output: Shuffled deck in an array

Contains:
    - value -> int: pre-calculate the value of the card, since that card is greater than 10 count as 0
    - deal -> Card: it will pop out a card from the list, Card is an Object

Author: Martin Chan
Created: 2026-11-20
"""

from dataclasses import dataclass, field 
import random

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]

@dataclass
class Card:
    """
    The Card class store the attributes of a card will have.
    Each card has a rank and the suit that stored in str.

    It has the value func for quick access to the card value that can be work out.
    Since the value is 0 if the card is greater than 10, and A count as 1.
    """

    rank: str
    suit: str

    @property 
    def value(self) -> int:
        if self.rank in ("10", "J", "Q", "K"):
            return 0
        if self.rank == "A":
            return 1
        return int(self.rank)

@dataclass 
class Deck:
    """
    Deck class main func is creating a list to representing the shuffled deck for later use.
    Pre-set the deck number as 8 which is normal number, and it can be change by calling it.

    post init -> it will run after the deck number is confirmed.
    """
    num_decks: int = 8 
    cards: list[Card] = field(init=False)

    def __post_init__(self):
        self.cards = [
            Card(rank, suit)
            for _ in range(self.num_decks)
            for rank in RANKS
            for suit in SUITS
        ]
        random.shuffle(self.cards)

    def count(self) -> int:
        return len(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

