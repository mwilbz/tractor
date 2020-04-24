from enum import Enum
from typing import Optional

from tractor.card import Card, Deck, Hand, Rank, Suit


class Team(Enum):
    ONE = 1
    TWO = 2


class Player:
    def __init__(self, team: Team):
        self.hand = Hand()
        self.team = team
    
    def draw(self, deck: Deck):
        self.hand.append_card(deck.draw())

    def sort_hand(self, trump_suit: Optional[Suit], trump_rank: Optional[Rank]):
        self.hand.sort(trump_suit, trump_rank)

    def __repr__(self):
        return f'<Player(team={self.team.value}, hand={self.hand})>'
