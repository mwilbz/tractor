from tractor.card import Card, Rank, Suit

def test_trick_comparator():
    comparator = Card.get_trick_comparator(trump_suit=Suit.CLUBS, trump_rank=Rank.SEVEN, trick_suit=Suit.DIAMONDS)
    assert 0 == comparator(
        Card(Suit.RED_JOKER, Rank.JOKER),
        Card(Suit.RED_JOKER, Rank.JOKER)
    )
    assert 1 == comparator(
        Card(Suit.RED_JOKER, Rank.JOKER),
        Card(Suit.BLACK_JOKER, Rank.JOKER)
    )
    assert -1 == comparator(
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.BLACK_JOKER, Rank.JOKER)
    )
    assert 1 == comparator(
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.CLUBS, Rank.ACE)
    )
    assert -1 == comparator(
        Card(Suit.CLUBS, Rank.EIGHT),
        Card(Suit.CLUBS, Rank.ACE)
    )
    assert 1 == comparator(
        Card(Suit.DIAMONDS, Rank.TWO),
        Card(Suit.SPADES, Rank.ACE)
    )
    assert 0 == comparator(
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.ACE)
    )
    assert 0 == comparator(
        Card(Suit.SPADES, Rank.SEVEN),
        Card(Suit.HEARTS, Rank.SEVEN)
    )
    assert -1 == comparator(
        Card(Suit.SPADES, Rank.SEVEN),
        Card(Suit.CLUBS, Rank.SEVEN)
    )
    assert -1 == comparator(
        Card(Suit.HEARTS, Rank.ACE),
        Card(Suit.SPADES, Rank.SEVEN)
    )


def test_sort_comparator():
    comparator = Card.get_sort_comparator(trump_suit=Suit.CLUBS, trump_rank=Rank.SEVEN, trick_suit=Suit.DIAMONDS)
    assert 0 == comparator(
        Card(Suit.RED_JOKER, Rank.JOKER),
        Card(Suit.RED_JOKER, Rank.JOKER)
    )
    assert 1 == comparator(
        Card(Suit.RED_JOKER, Rank.JOKER),
        Card(Suit.BLACK_JOKER, Rank.JOKER)
    )
    assert -1 == comparator(
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.BLACK_JOKER, Rank.JOKER)
    )
    assert 1 == comparator(
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.CLUBS, Rank.ACE)
    )
    assert -1 == comparator(
        Card(Suit.CLUBS, Rank.EIGHT),
        Card(Suit.CLUBS, Rank.ACE)
    )
    assert 1 == comparator(
        Card(Suit.DIAMONDS, Rank.TWO),
        Card(Suit.SPADES, Rank.ACE)
    )
    assert 1 == comparator(
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.ACE)
    )
    assert 0 == comparator(
        Card(Suit.SPADES, Rank.SEVEN),
        Card(Suit.HEARTS, Rank.SEVEN)
    )
    assert -1 == comparator(
        Card(Suit.SPADES, Rank.SEVEN),
        Card(Suit.CLUBS, Rank.SEVEN)
    )
    assert -1 == comparator(
        Card(Suit.HEARTS, Rank.ACE),
        Card(Suit.SPADES, Rank.SEVEN)
    )
