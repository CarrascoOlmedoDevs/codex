# Football Manager Simulator

A simple European football (soccer) manager game with a 2D match engine using Python and Pygame.

## Features
- Real-time match engine with 11 vs 11 players.
- Basic AI for attacking, defending, passing and shooting.
- 2D top-down visualization built with Pygame.
- Tactical controls for formation and mentality (press keys `f` and `m`).
- Random match events (goals, fouls, offsides, injuries).
- Editable team rosters via `data/teams.json` and `team_editor.py`.
- Fast simulation mode using `python main.py --fast`.

## Running
```
python main.py            # watch the match
python main.py --fast     # simulate instantly
```

## Editing Teams
```
python team_editor.py home NewPlayer MF 70 70 50 50 90
```
This adds a new player to the home team.

The project is modular to allow future expansion such as tournaments, transfers, training and club management.

## WhatsApp + MCP Integration
To execute approved commands from WhatsApp through an MCP bridge, see:

- `integrations/README_whatsapp_mcp.md`
- `integrations/whatsapp_mcp_bridge.py`
