"""One barrier: its surface, mask and erosion on hit (R3).

Key design decision (document the options on the wiki):
- Block grid: a 2D grid of small blocks; a hit removes nearby blocks.
- Pixel erosion: own Surface + pygame.mask.Mask; draw a transparent "bite"
  at the impact point and rebuild the mask.
- Health states: swap between damage images (weakest option).

Remember the coordinate transform: screen coordinates -> barrier-local.
"""

import pygame


class Barrier(pygame.sprite.Sprite):
    """A single destructible barrier."""

    def __init__(self, x, y):
        """TODO: build the image/surface (or block grid), rect and mask."""
        super().__init__()

    def hit(self, point, from_above):
        """Erode the barrier at a screen-space point.

        from_above: True for invader bullets, False for player bullets, so the
        bite shape can be directional.
        """
        pass

    def is_solid_at(self, point):
        """Return True if there is barrier left at this screen-space point.

        A bullet over an already destroyed gap should pass through.
        """
        raise NotImplementedError

    def erase_overlap(self, rect):
        """Erase the parts of the barrier an invader overlaps."""
        pass

    def is_destroyed(self):
        """Return True when nothing of the barrier is left."""
        raise NotImplementedError
