import random
from typing import List

from .ball import Ball
from .player import Player
from .team import Team
from .constants import FIELD_WIDTH, FIELD_HEIGHT, GOAL_WIDTH

class MatchEngine:
    """Simple football match engine."""

    def __init__(self, home: Team, away: Team):
        self.home = home
        self.away = away
        self.ball = Ball()
        self.time = 0.0
        self.events: List[str] = []
        self.running = True
        self.home.reset_positions()
        self.away.reset_positions()

    def step(self, dt: float) -> None:
        """Advance simulation by dt seconds."""
        self.time += dt
        self.ball.update(dt)
        players = self.home.players + self.away.players
        for p in players:
            self.update_player(p, dt)
        self.check_goals()
        self.random_events()

    def update_player(self, player: Player, dt: float) -> None:
        if player.has_ball:
            target_goal_x = FIELD_WIDTH if player.team is self.home else 0
            # decide to shoot if close
            if abs(player.x - target_goal_x) < 150 and random.random() < player.shooting / 100:
                self.shoot(player)
            else:
                teammate = random.choice(player.team.players)
                self.pass_ball(player, teammate)
        else:
            if self.is_nearest_player(player):
                player.move_towards((self.ball.x, self.ball.y), dt)
                if self.distance(player.x, player.y, self.ball.x, self.ball.y) < 10:
                    player.has_ball = True
            else:
                player.move_towards((player.x, player.y), dt)  # keep position

    def is_nearest_player(self, player: Player) -> bool:
        dist = self.distance(player.x, player.y, self.ball.x, self.ball.y)
        players = player.team.players
        return all(dist <= self.distance(o.x, o.y, self.ball.x, self.ball.y) for o in players)

    def pass_ball(self, passer: Player, receiver: Player) -> None:
        passer.has_ball = False
        receiver.has_ball = True
        self.ball.x, self.ball.y = receiver.x, receiver.y
        self.events.append(f"{passer.name} passes to {receiver.name}")

    def shoot(self, player: Player) -> None:
        player.has_ball = False
        goal_x = FIELD_WIDTH if player.team is self.home else 0
        self.ball.x, self.ball.y = goal_x, random.uniform(FIELD_HEIGHT/2 - GOAL_WIDTH/2,
                                                         FIELD_HEIGHT/2 + GOAL_WIDTH/2)
        if random.random() < 0.02:
            player.team.score += 1
            self.events.append(f"Goal by {player.name} for {player.team.name}")
        else:
            self.events.append(f"Shot by {player.name} saved")
        self.ball = Ball()
        self.home.reset_positions()
        self.away.reset_positions()

    def check_goals(self) -> None:
        # Ball outside field resets
        if not (0 <= self.ball.x <= FIELD_WIDTH) or not (0 <= self.ball.y <= FIELD_HEIGHT):
            self.ball = Ball()
            self.home.reset_positions()
            self.away.reset_positions()

    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float) -> float:
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def random_events(self) -> None:
        """Generate random fouls, offsides and injuries."""
        r = random.random()
        if r < 0.001:
            offender = random.choice(self.home.players + self.away.players)
            self.events.append(f"Foul committed by {offender.name}")
        elif r < 0.002:
            offside = random.choice(self.home.players + self.away.players)
            self.events.append(f"Offside by {offside.name}")
        elif r < 0.0025:
            injured = random.choice(self.home.players + self.away.players)
            self.events.append(f"{injured.name} is injured")
