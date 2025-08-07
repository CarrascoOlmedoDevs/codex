import json
from dataclasses import dataclass, field
from typing import List

from .player import Player

@dataclass
class Team:
    name: str
    players: List[Player] = field(default_factory=list)
    formation: str = "4-4-2"
    mentality: str = "balanced"  # defensive, offensive
    score: int = 0

    @classmethod
    def from_json(cls, path: str) -> "Team":
        with open(path, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict) -> "Team":
        players = [Player(**p) for p in data['players']]
        team = cls(name=data['name'], players=players)
        for p in team.players:
            p.team = team
        return team

    def reset_positions(self) -> None:
        """Reset players to default formation positions."""
        # Simple layout: divide field into grid per formation string
        formation_map = {
            "4-4-2": [(100, 340), (200, 200), (200, 480), (350, 120), (350, 340), (350, 560),
                       (500, 200), (500, 480), (650, 340), (800, 200), (800, 480)],
            "4-3-3": [(100, 340), (200, 200), (200, 480), (350, 120), (350, 340), (350, 560),
                       (500, 340), (650, 200), (650, 480), (800, 200), (800, 480)],
        }
        layout = formation_map.get(self.formation, formation_map["4-4-2"])
        for player, pos in zip(self.players, layout):
            player.x, player.y = pos
