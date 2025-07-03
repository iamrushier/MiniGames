import random
from .card import Card
class Deck:
    # Constants
    SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self) -> None:
        self.cards = [Card(suit, value) for suit in Deck.SUITS for value in Deck.VALUES]

    # Shuffle if two or more cards
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)