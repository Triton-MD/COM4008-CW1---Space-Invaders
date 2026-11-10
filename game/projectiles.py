"""Bullets: the shared Bullet base class, PlayerBullet and InvaderBullet.

SHARED FILE: R1 and R2 both subclass Bullet, so agree this interface in
week 1 and change it only through a reviewed PR.

Agreed interface:
- rect       position and size (from pygame.sprite.Sprite)
- velocity   pixels per second (negative = up)
- owner      "player" or "invader"
- update(dt) move by velocity * dt, and kill() when off screen so the
             sprite group never grows forever
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    """Base class for every projectile in the game."""

    def __init__(self, x, y, velocity, owner):
        """Create a bullet at (x, y) moving at velocity px/s, fired by owner.

        TODO: call super().__init__(), build self.image and self.rect,
        store velocity and owner.
        """
        super().__init__()

    def update(self, dt):
        """Move by velocity * dt; remove self with kill() once off screen."""
        pass


class PlayerBullet(Bullet):
    """A bullet fired upwards by the player (R2)."""

    pass


class InvaderBullet(Bullet):
    """A bullet fired downwards by an invader (R1)."""

    pass
