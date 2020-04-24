import time
from typing import Dict, List

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
DEAL_PAUSE_BETWEEN_CARDS_SECONDS = .3


class Game:
    def __init__(self):
        self.deck: Deck = None
        self.players: List[Player] = [
            Player(team=Team.ONE),
            Player(team=Team.TWO),
            Player(team=Team.ONE),
            Player(team=Team.TWO)
        ]
        self.scores: Dict[Team, Rank] = {
            Team.ONE: Rank.TWO,
            Team.TWO: Rank.TWO
        }
        self.declarers: Team = Team.ONE
        self.trump_suit = None
    
    def pause_for_trump_declaration(self):
        time.sleep(DEAL_PAUSE_BETWEEN_CARDS_SECONDS)

    def deal_cards(self):
        print('Dealing hands!')
        for _ in range(25):
            for player_index in range(4):
                self.players[player_index].draw(self.deck)
                self.players[player_index].sort_hand(trump_suit=None, trump_rank=self.scores[self.declarers])
                self.pause_for_trump_declaration()
                print(self.players[player_index])
    
    def play_round(self):
        self.deck = initialize_deck()
        self.trump_suit = None
        self.deal_cards()
        print(f'Deck: {self.deck}')
        print(f'Players: {self.players}')
        input('Pausing for input')
    
    def start(self):
        while True:
            if self.scores[Team.ONE] == Rank.JOKER:
                print('Team One wins!')
                return
            if self.scores[Team.TWO] == Rank.JOKER:
                print('Team Two wins!')
                return

            self.play_round()


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
