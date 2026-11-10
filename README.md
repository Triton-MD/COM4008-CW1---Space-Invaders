# Space Defenders

COM4008 CW1: a Space Invaders-style game in Python and pygame.

## Team and requirement ownership

| Member | Requirement | Folder |
|--------|-------------|--------|
| TODO   | R1 Invader fleet | `game/fleet/` |
| TODO   | R2 Player combat | `game/player/` |
| TODO   | R3 Barriers      | `game/barriers/` |

## Install

```
pip install -r requirements.txt
```

## Run the game

Always run from the project root:

```
python main.py
```

## Run the tests

```
pytest
```

Tests run headless (no window), so they also run in GitHub Actions on every pull request.

## Project layout

- `main.py`: entry point
- `settings.py`: every tweakable number
- `game/`: all game code, one sub-package per requirement
- `assets/`: our own images, sounds and fonts (see `assets/CREDITS.md`)
- `tests/`: one test file per module
- `docs/diagrams/`: images linked from the wiki

Design, testing and the dev log live on the GitHub wiki.
