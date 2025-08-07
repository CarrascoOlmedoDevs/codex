from dataclasses import dataclass

@dataclass
class Ball:
    x: float = 525
    y: float = 340
    vx: float = 0.0
    vy: float = 0.0

    def update(self, dt: float) -> None:
        """Update ball position with simple friction."""
        self.x += self.vx * dt
        self.y += self.vy * dt
        # friction
        self.vx *= 0.99
        self.vy *= 0.99
