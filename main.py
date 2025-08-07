import argparse
import json
import pygame

from game.constants import FPS
from game.engine import MatchEngine
from game.team import Team
from game.visual import Renderer
from game.manager import Manager


def load_teams(path: str):
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return Team.from_dict(data['home']), Team.from_dict(data['away'])


def run_match(fast: bool = False, speed: float = 1.0):
    home, away = load_teams('data/teams.json')
    engine = MatchEngine(home, away)
    if fast:
        dt = 1.0 * speed
        total_time = 90 * 60
        while engine.time < total_time:
            engine.step(dt)
        print(f"Final score: {home.name} {home.score} - {away.score} {away.name}")
        return

    renderer = Renderer(engine)
    clock = pygame.time.Clock()
    home_manager = Manager(home)
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0 * speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    new_form = '4-3-3' if home.formation == '4-4-2' else '4-4-2'
                    home_manager.set_formation(new_form)
                elif event.key == pygame.K_m:
                    home_manager.set_mentality('offensive' if home.mentality != 'offensive' else 'defensive')
        engine.step(dt)
        renderer.draw()
        for e in engine.events[-5:]:
            print(e)
    pygame.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Football simulator')
    parser.add_argument('--fast', action='store_true', help='simulate quickly without graphics')
    parser.add_argument('--speed', type=float, default=1.0, help='simulation speed multiplier')
    args = parser.parse_args()
    run_match(fast=args.fast, speed=args.speed)
