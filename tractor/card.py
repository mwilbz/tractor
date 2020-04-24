from enum import Enum
import random
from typing import List


class Suit(Enum):
    HEARTS = 'HEARTS'
    DIAMONDS = 'DIAMONDS'
    SPADES = 'SPADES'
    CLUBS = 'CLUBS'
    RED_JOKER = 'RED_JOKER'
    BLACK_JOKER = 'BLACK_JOKER'

    def __repr__(self):
        if self.value == 'HEARTS':
            return '❤️'
        if self.value == 'DIAMONDS':
            return '♦️'
        if self.value == 'SPADES':
            return '♠️'
        if self.value == 'CLUBS':
            return '♣️'
        if self.value == 'RED_JOKER':
            return '🟥'
        if self.value == 'BLACK_JOKER':
            return '⬛️'


class Rank(Enum):
    JOKER = 15
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

    def __repr__(self):
        if self.value == 15:
            return 'Joker'
        if self.value == 14:
            return 'A'
        if self.value == 13:
            return 'K'
        if self.value == 12:
            return 'Q'
        if self.value == 11:
            return 'J'
        
        return repr(self.value)


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        is_joker_suit = suit in [Suit.BLACK_JOKER, Suit.RED_JOKER]
        is_joker_rank = rank == Rank.JOKER
        if is_joker_suit != is_joker_rank:
            raise Exception(f'Suit was {suit} but rank was {rank}')

        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{repr(self.rank)}{repr(self.suit)}'


class CardGroup:
    def __init__(self):
        self.cards: List[Card] = []

    def append_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card_index):
        if len(self.cards) < 1:
            raise Exception('{self.__class__.__name__} is empty!')
        self.cards.pop(card_index)
    
    def sort(self):
        self.cards = sorted(self.cards)

    def __repr__(self):
        return f'<{len(self.cards)} card(s): {repr(self.cards)}>'


class Hand(CardGroup):
    pass


class Deck(CardGroup):
    def draw(self) -> Card:
        if len(self.cards) < 1:
            raise Exception('Deck is empty!')

        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)
