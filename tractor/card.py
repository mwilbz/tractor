from enum import Enum
from functools import cmp_to_key
import random
from typing import List, Optional


class Suit(Enum):
    HEARTS = 3
    DIAMONDS = 2
    SPADES = 4
    CLUBS = 1
    BLACK_JOKER = 5
    RED_JOKER = 6

    @staticmethod
    def sort_compare(suit1, suit2):
        if suit1.value > suit2.value:
            return 1
        if suit1.value < suit2.value:
            return -1

        return 0

    def __repr__(self):
        if self == Suit.HEARTS:
            return '❤️'
        if self == Suit.DIAMONDS:
            return '♦️'
        if self == Suit.SPADES:
            return '♠️'
        if self == Suit.CLUBS:
            return '♣️'
        if self == Suit.RED_JOKER:
            return '🟥'
        if self == Suit.BLACK_JOKER:
            return '⬛️'
        
        raise Exception('Got unexpected value for Suit enum')


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

    @staticmethod
    def sort_compare(rank1, rank2):
        if rank1.value > rank2.value:
            return 1
        if rank1.value < rank2.value:
            return -1

        return 0

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

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.suit == other.suit and self.rank == other.rank
    
    @staticmethod
    def get_trick_comparator(trump_suit: Suit, trump_rank: Rank, trick_suit: Suit):
        def comparator(card1: Card, card2: Card):
            if card1 == card2:
                return 0

            if card1.suit == Suit.RED_JOKER:
                return 1
            if card2.suit == Suit.RED_JOKER:
                return -1
            
            if card1.suit == Suit.BLACK_JOKER:
                return 1
            if card2.suit == Suit.BLACK_JOKER:
                return -1
            
            if card1.rank == trump_rank and card2.rank == trump_rank:
                if card1.suit == trump_suit:
                    return 1
                if card2.suit == trump_suit:
                    return -1
                
                return 0
            if card1.rank == trump_rank:
                return 1
            if card2.rank == trump_rank:
                return -1

            if card1.suit == trump_suit and card2.suit == trump_suit:
                if card1.rank == trump_rank:
                    return 1
                if card2.rank == trump_rank:
                    return -1
                
                if card1.rank.value > card2.rank.value:
                    return 1
                else:
                    return -1
            
            if card1.suit == trump_suit:
                return 1
            if card2.suit == trump_suit:
                return -1
            
            if card1.suit == trick_suit and card2.suit == trick_suit:
                if card1.rank.value > card2.rank.value:
                    return 1
                else:
                    return -1
            
            if card1.suit == trick_suit:
                return 1
            if card2.suit == trick_suit:
                return -1

            return 0
        
        return comparator
    
    @staticmethod
    def get_sort_comparator(trump_suit: Optional[Suit], trump_rank: Optional[Rank]):
        def comparator(card1: Card, card2: Card):
            if card1 == card2:
                return 0

            if card1.suit == Suit.RED_JOKER:
                return 1
            if card2.suit == Suit.RED_JOKER:
                return -1
            
            if card1.suit == Suit.BLACK_JOKER:
                return 1
            if card2.suit == Suit.BLACK_JOKER:
                return -1
            
            if trump_rank is not None:
                if card1.rank == trump_rank and card2.rank == trump_rank:
                    if trump_suit is None:
                        return 0
                    if card1.suit == trump_suit:
                        return 1
                    if card2.suit == trump_suit:
                        return -1
                    
                    return 0
                if card1.rank == trump_rank:
                    return 1
                if card2.rank == trump_rank:
                    return -1
            
            if trump_suit is not None:
                if card1.suit == trump_suit and card2.suit == trump_suit:
                    if card1.rank == trump_rank:
                        return 1
                    if card2.rank == trump_rank:
                        return -1
                    
                    if card1.rank.value > card2.rank.value:
                        return 1
                    else:
                        return -1
                
                if card1.suit == trump_suit:
                    return 1
                if card2.suit == trump_suit:
                    return -1

            suit_comparison = Suit.sort_compare(card1.suit, card2.suit)
            if suit_comparison != 0:
                return suit_comparison
            
            return Rank.sort_compare(card1.rank, card2.rank)
        
        return comparator

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
    
    def sort(self, trump_suit: Optional[Suit], trump_rank: Optional[Rank]):
        self.cards = sorted(self.cards, key=cmp_to_key(Card.get_sort_comparator(trump_suit=trump_suit, trump_rank=trump_rank)))

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
