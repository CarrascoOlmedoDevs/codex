from dataclasses import dataclass, field
from typing import Tuple

@dataclass
class Player:
    """Represents a football player."""

    name: str
    position: str
    speed: float
    passing: float
    shooting: float
    defense: float
    stamina: float
    x: float = 0
    y: float = 0
    has_ball: bool = False
    state: str = "idle"  # attacking, defending, pressing
    team: "Team" = field(repr=False, default=None)

    def move_towards(self, target: Tuple[float, float], dt: float) -> None:
        """Move the player toward a target position."""
        tx, ty = target
        dx = tx - self.x
        dy = ty - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 1e-5:
            step = min(self.speed * dt, dist)
            self.x += dx / dist * step
            self.y += dy / dist * step
