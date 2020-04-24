from typing import List

from tractor.card import Card, Deck, Rank, Suit
from tractor.player import Player, Team


NUM_DECKS = 2
NON_JOKER_RANKS = [
    Rank.ACE,
    Rank.KING,
    Rank.QUEEN,
    Rank.JACK,
    Rank.TEN,
    Rank.NINE,
    Rank.EIGHT,
    Rank.SEVEN,
    Rank.SIX,
    Rank.FIVE,
    Rank.FOUR,
    Rank.THREE,
    Rank.TWO
]


class Game:
    def __init__(self):
        self.deck: Deck = initialize_deck()
        self.players: List[Player] = [
            Player(team=Team.ONE),
            Player(team=Team.TWO),
            Player(team=Team.ONE),
            Player(team=Team.TWO)
        ]

    def deal_cards(self):
        for _ in range(25):
            for player_index in range(4):
                self.players[player_index].draw(self.deck)
        
        for player in self.players:
            player.sort_hand()
    
    def start(self):
        self.deal_cards()
        print(f'Deck: {self.deck}')
        print(f'Players: {self.players}')


def initialize_deck() -> Deck:
    deck = Deck()
    for suit in [Suit.BLACK_JOKER, Suit.RED_JOKER]:
        for _ in range(NUM_DECKS):
            deck.append_card(Card(
                suit=suit,
                rank=Rank.JOKER
            ))
    
    for suit in [Suit.HEARTS, Suit.DIAMONDS, Suit.SPADES, Suit.CLUBS]:
        for rank in NON_JOKER_RANKS:
            for _ in range(NUM_DECKS):
                deck.append_card(Card(
                    suit=suit,
                    rank=rank
                ))
    
    deck.shuffle()
    
    return deck
