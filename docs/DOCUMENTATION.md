# Space Defenders: technical documentation

In-repo reference for anyone working on the code. Design reasoning, testing
evidence and the dev log live on the GitHub wiki (drafts in `wiki/`); this file
explains how the code fits together.

## 1. Overview

<!-- What the game does, in a few sentences. Game name and version. -->

## 2. Getting started

- Requirements: Python 3.x, see `requirements.txt`
- Run: `python main.py` from the project root
- Test: `pytest`
<!-- Add controls: which keys move, fire, pause. -->

## 3. Architecture

<!-- How main.py, Game, states, the requirement packages and collisions.py
connect. Link a diagram from docs/diagrams/. -->

### Main loop

<!-- handle_events -> update(dt) -> collisions.resolve -> draw -->

### Game states

<!-- MENU, PLAYING, RESPAWNING, GAME_OVER and the transitions. -->

## 4. Modules

| Module | Owner | Responsibility |
|--------|-------|----------------|
| `game/game.py` | Shared | Main loop, owns sprite groups |
| `game/states.py` | Shared | State machine |
| `game/projectiles.py` | Shared | Bullet classes |
| `game/collisions.py` | Shared | Collision step |
| `game/hud.py` | | Score, lives, wave |
| `game/assets.py` | | Loads images, sounds, fonts |
| `game/fleet/` | R1 | Invaders and fleet |
| `game/player/` | R2 | Player ship |
| `game/barriers/` | R3 | Barriers |

## 5. Shared interfaces

<!-- Public methods each part relies on, with arguments and return values. -->

## 6. Configuration

<!-- Key values in settings.py and what changing them does. -->

## 7. Assets

<!-- Naming convention (lowercase_with_underscores_frame.png), where each kind
of asset lives, and a pointer to assets/CREDITS.md. -->

## 8. Testing

<!-- How tests are organised, headless setup, CI. Link the wiki Testing page. -->

## 9. Known issues and limitations

## 10. Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1-stubs | | Repository structure and stubs |
