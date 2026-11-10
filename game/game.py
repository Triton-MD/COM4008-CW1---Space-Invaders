"""The Game class: the main loop and the owner of every sprite group.

SHARED FILE: everyone edits this, so changes go through a reviewed PR.

Responsibilities:
- Initialise pygame, the window and the clock.
- Own the shared groups: player_bullets, enemy_bullets, barriers (nobody else
  creates their own global lists).
- Own the fleet, the player, the score and the current state.
- Each frame: handle events -> update(dt) -> run the collision step -> draw.
"""

import pygame

import settings


class Game:
    """Holds the whole game world and runs the main loop."""

    def __init__(self):
        """Set up pygame, the screen, the clock and the game objects.

        TODO:
        - pygame.init(), create the screen from settings.SCREEN_WIDTH/HEIGHT
        - create the clock
        - create the shared sprite groups (player_bullets, enemy_bullets, barriers)
        - create the Fleet (R1), Player (R2) and BarrierRow (R3)
        - set score, wave and the starting state (see states.py)
        """
        pass

    def run(self):
        """Main loop: keep going until the player quits.

        TODO: each iteration
        - dt = self.clock.tick(settings.FPS) / 1000   (seconds since last frame)
        - self.handle_events()
        - self.update(dt)
        - self.draw()
        Multiply every speed by dt so movement is frame-rate independent.
        """
        raise NotImplementedError

    def handle_events(self):
        """Process the pygame event queue (quit, pause, menu keys).

        Held keys (moving, holding fire) are read with
        pygame.key.get_pressed() inside Player.update, not here.
        """
        pass

    def update(self, dt):
        """Advance the world by dt seconds, then run the one collision step.

        TODO: update groups, call collisions.resolve(...) once, check for
        wave cleared / game over and switch state if needed.
        """
        pass

    def draw(self):
        """Draw the current frame: background, sprites, HUD, then flip."""
        pass
