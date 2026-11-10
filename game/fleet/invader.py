"""One invader: its kind, points value and animation frames (R1).

Design choice to explain in the demo: one Invader class plus a data table
(kind -> sprite names, points) rather than three subclasses, because the
three kinds behave the same and only their data differs.
"""

import pygame

# TODO: kind -> data table, for example
# INVADER_TYPES = {
#     0: {"frames": ["invader_a_1", "invader_a_2"], "points": 10},
#     1: {"frames": ["invader_b_1", "invader_b_2"], "points": 20},
#     2: {"frames": ["invader_c_1", "invader_c_2"], "points": 30},
# }


class Invader(pygame.sprite.Sprite):
    """A single alien in the fleet."""

    def __init__(self, kind, x, y):
        """Create an invader of the given kind at (x, y).

        TODO: store kind, look up points and frames, set image and rect.
        """
        super().__init__()

    def animate(self):
        """Swap to the next animation frame (called when the fleet steps)."""
        pass
