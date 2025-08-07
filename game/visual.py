import pygame

from .constants import (BLACK, BLUE, FIELD_HEIGHT, FIELD_WIDTH, GREEN, RED,
                        WHITE, PLAYER_RADIUS, BALL_RADIUS)
from .engine import MatchEngine

class Renderer:
    """Handles Pygame rendering of the match."""

    def __init__(self, engine: MatchEngine):
        pygame.init()
        self.engine = engine
        self.screen = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))
        pygame.display.set_caption("Football Simulator")
        self.font = pygame.font.SysFont(None, 24)

    def draw(self) -> None:
        self.screen.fill(GREEN)
        pygame.draw.line(self.screen, WHITE, (FIELD_WIDTH/2, 0), (FIELD_WIDTH/2, FIELD_HEIGHT), 2)
        self.draw_players()
        self.draw_ball()
        self.draw_scoreboard()
        pygame.display.flip()

    def draw_players(self) -> None:
        for p in self.engine.home.players:
            pygame.draw.circle(self.screen, BLUE, (int(p.x), int(p.y)), PLAYER_RADIUS)
        for p in self.engine.away.players:
            pygame.draw.circle(self.screen, RED, (int(p.x), int(p.y)), PLAYER_RADIUS)

    def draw_ball(self) -> None:
        pygame.draw.circle(self.screen, WHITE, (int(self.engine.ball.x), int(self.engine.ball.y)), BALL_RADIUS)

    def draw_scoreboard(self) -> None:
        txt = self.font.render(f"{self.engine.home.name} {self.engine.home.score} - {self.engine.away.score} {self.engine.away.name}", True, BLACK)
        self.screen.blit(txt, (FIELD_WIDTH/2 - txt.get_width()/2, 5))
        time_txt = self.font.render(f"{int(self.engine.time)}s", True, BLACK)
        self.screen.blit(time_txt, (10, 5))
