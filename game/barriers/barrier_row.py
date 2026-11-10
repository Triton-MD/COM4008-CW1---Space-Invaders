"""Builds and spaces the four barriers (R3).

Positions are computed from the screen width, not hard-coded, so the
barriers stay evenly spaced if the window size changes.
"""


def build_barriers(screen_width, y, count=4):
    """Return a pygame.sprite.Group of `count` evenly spaced Barrier objects.

    TODO: work out the gap between barriers from screen_width and count.
    """
    raise NotImplementedError
