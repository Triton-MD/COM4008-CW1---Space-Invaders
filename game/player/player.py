"""The player's ship: movement, shooting cooldown, lives and respawn (R2).

Read held keys with pygame.key.get_pressed(), not just KEYDOWN events, so
holding fire shoots continuously (gated by a cooldown timer).
"""

import pygame


class Player(pygame.sprite.Sprite):
    """The player-controlled ship."""

    def __init__(self):
        """TODO: image, rect at the bottom centre, lives, cooldown timer,
        invulnerability timer."""
        super().__init__()

    def update(self, dt, player_bullets):
        """Move left/right (clamped to the screen) and fire if allowed.

        Hint: rect.clamp_ip(screen_rect) keeps the ship on screen.
        """
        pass

    def can_fire(self):
        """Return True if the shot cooldown has finished (and under bullet cap)."""
        raise NotImplementedError

    def on_hit(self):
        """Callback from collisions.py: lose a life unless invulnerable.

        Edge case to test: a second hit during invulnerability does nothing.
        """
        pass

    def respawn(self):
        """Return to the centre with a short invulnerability window."""
        pass

    def is_dead(self):
        """Return True when lives have run out."""
        raise NotImplementedError
