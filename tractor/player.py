from enum import Enum

from tractor.card import Hand


class Team(Enum):
    ONE = 1
    TWO = 2


class Player:
    def __init__(self, team: Team):
        self.hand = Hand()
        self.team = team

    def __repr__(self):
        return f'<Player(team={self.team}, hand={self.hand})>'
