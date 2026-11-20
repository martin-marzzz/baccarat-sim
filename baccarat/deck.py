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

    def deal(self) -> Card:
        return self.cards.pop()

