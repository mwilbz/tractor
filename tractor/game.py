from card import Deck, Rank, Suit
from player import Player, Team


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
        self.players = [
            Player(team=Team.ONE),
            Player(team=Team.TWO),
            Player(team=Team.ONE),
            Player(team=Team.TWO)
        ]


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
    
    return deck


