"""Simple team editor script."""
import json
from pathlib import Path

DATA_FILE = Path("data/teams.json")

def list_teams() -> None:
    data = json.loads(DATA_FILE.read_text())
    for side, info in data.items():
        print(side, info["name"])  # type: ignore

def add_player(team_side: str, player: dict) -> None:
    data = json.loads(DATA_FILE.read_text())
    data[team_side]["players"].append(player)
    DATA_FILE.write_text(json.dumps(data, indent=2))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("team")
    parser.add_argument("name")
    parser.add_argument("position")
    parser.add_argument("speed", type=int)
    parser.add_argument("passing", type=int)
    parser.add_argument("shooting", type=int)
    parser.add_argument("defense", type=int)
    parser.add_argument("stamina", type=int)
    args = parser.parse_args()
    player = {
        "name": args.name,
        "position": args.position,
        "speed": args.speed,
        "passing": args.passing,
        "shooting": args.shooting,
        "defense": args.defense,
        "stamina": args.stamina,
    }
    add_player(args.team, player)
    list_teams()
