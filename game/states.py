"""Game states: menu, playing, respawning, game over.

A small state machine is cleaner than a pile of booleans
(is_paused, is_dead, is_menu...), and it is a strong concept for the demo.

Suggested states: MENU, PLAYING, RESPAWNING, GAME_OVER
(optionally PAUSED, HIGH_SCORE_ENTRY).
"""

from enum import Enum, auto


class State(Enum):
    """Every state the game can be in. Game holds exactly one at a time."""

    MENU = auto()
    PLAYING = auto()
    RESPAWNING = auto()
    GAME_OVER = auto()


# TODO: decide which transitions are allowed, for example
#   MENU -> PLAYING          (press start)
#   PLAYING -> RESPAWNING    (player hit, lives left)
#   RESPAWNING -> PLAYING    (respawn timer finished)
#   PLAYING -> GAME_OVER     (lives == 0, or invaders reach the player row)
#   GAME_OVER -> MENU
# You could keep a dict of allowed transitions here and test it.
