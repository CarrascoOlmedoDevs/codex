from typing import Dict, List

from .player import Player
from .team import Team

class Manager:
    """Controls team tactics and substitutions."""

    def __init__(self, team: Team):
        self.team = team
        self.substitutes: List[Player] = []

    def set_formation(self, formation: str) -> None:
        self.team.formation = formation
        self.team.reset_positions()

    def set_mentality(self, mentality: str) -> None:
        self.team.mentality = mentality

    def make_substitution(self, out_player: Player, in_player: Player) -> None:
        if out_player in self.team.players and in_player in self.substitutes:
            idx = self.team.players.index(out_player)
            self.team.players[idx] = in_player
            self.substitutes.remove(in_player)
            self.substitutes.append(out_player)
            self.team.reset_positions()
