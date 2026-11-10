"""The invader fleet: the 2D grid, movement, edge bounce, speed-up and firing (R1).

Keep both:
- a pygame.sprite.Group of invaders, for drawing and collisions
- a grid[row][col] list (None where an invader died), for column logic.
  The grid is "the full invaders array" the requirement asks for.

Keep rules in plain methods that need no window (e.g. current_speed() returns
a number) so tests can call them directly.
"""


class Fleet:
    """All the invaders, moving and firing as one unit."""

    def __init__(self, rng=None):
        """Build the grid from settings.FLEET_LAYOUT.

        rng: a random.Random(seed) object, passed in so tests can make
        firing predictable.
        TODO: build grid and group, set direction, record the starting total.
        """
        pass

    def update(self, dt, enemy_bullets):
        """Move the fleet, bounce at the edges and maybe fire.

        TODO: move by current_speed() * dt; if the leftmost/rightmost LIVING
        invader would cross the edge, reverse and drop. (Common bug: using the
        original grid edges, so the fleet bounces early once a column is gone.)
        """
        pass

    def current_speed(self):
        """Return the fleet's speed, which rises as invaders are destroyed.

        Pick a formula and justify it on the wiki (linear vs ratio-based),
        and cap the maximum. Must not divide by zero when none are alive.
        """
        raise NotImplementedError

    def shooters(self):
        """Return the bottom-most living invader in each column.

        Only these may fire, so aliens never shoot through each other.
        """
        raise NotImplementedError

    def on_invader_destroyed(self, invader):
        """Callback from collisions.py: remove the invader from the grid."""
        pass

    def reached_bottom(self, y_limit):
        """Return True if any invader has reached the player's row."""
        raise NotImplementedError

    def alive_count(self):
        """Return how many invaders are still alive."""
        raise NotImplementedError
