"""The invader fleet: the 2D grid, movement, edge bounce, speed-up and firing (R1).

The fleet keeps two views of the same invaders:
- self.invaders: a pygame.sprite.Group, for drawing and collisions
- self.grid[row][col]: a 2D list (None where an invader died), for column
  logic such as "which invader is at the bottom of column 3?". The grid is
  "the full invaders array" the requirement asks for.

The fleet moves, not the invaders: each invader has a fixed home position and
the fleet keeps one float offset. rect.x is an int, so moving rects directly
by less than 1 px per frame would round to 0 and the fleet would never move.

Game rules (current_speed, shooters, living_bounds...) need no window, so the
tests call them directly.
"""

import random

import pygame

import settings
from game.fleet.invader import Invader
from game.projectiles import InvaderBullet


class Fleet:
    """All the invaders, moving and firing as one unit."""

    def __init__(self, rng: random.Random | None = None):
        """Build the grid from settings.FLEET_LAYOUT.

        rng: a random.Random object. Tests pass random.Random(seed) so firing
        is the same on every run; the game passes random.Random().
        """
        self.rng = rng if rng is not None else random.Random()
        self.invaders = pygame.sprite.Group()
        self.grid: list[list[Invader | None]] = []
        for row, kind in enumerate(settings.FLEET_LAYOUT):
            grid_row = []
            for col in range(settings.FLEET_COLS):
                x = settings.FLEET_START_X + col * settings.FLEET_H_SPACING
                y = settings.FLEET_START_Y + row * settings.FLEET_V_SPACING
                invader = Invader(kind, row, col, x, y)
                grid_row.append(invader)
                self.invaders.add(invader)
            self.grid.append(grid_row)

        self.start_total = len(self.invaders) # 55: used by the speed formula
        self.direction = 1 # 1 = right, -1 = left
        self.offset_x = 0.0 # float offsets, see module docstring
        self.offset_y = 0.0
        self.fire_timer = self._next_fire_delay()
        self.anim_timer = 0.0

    # Rules (no window needed, tested directly)
    def alive_count(self) -> int:
        """Return how many invaders are still alive."""
        return len(self.invaders)

    def current_speed(self) -> float:
        """Return the fleet's speed in px/s, which rises as invaders are destroyed.

        Ratio formula: base * start_total / alive, capped at FLEET_MAX_SPEED.
        Slow for most of the wave, then a rush near the end. Returns 0 when
        no invaders are alive, so there is never a division by zero.
        """
        alive = self.alive_count()
        if alive == 0:
            return 0.0
        speed = settings.FLEET_BASE_SPEED * self.start_total / alive
        return min(speed, settings.FLEET_MAX_SPEED)

    def shooters(self) -> list[Invader]:
        """Return the bottom-most living invader in each column.

        Only these may fire, so aliens never shoot through each other.
        """
        result = []
        for col in range(settings.FLEET_COLS):
            for row in range(len(self.grid) - 1, -1, -1): # bottom row upwards
                invader = self.grid[row][col]
                if invader is not None:
                    result.append(invader)
                    break # this column is done
        return result

    def living_bounds(self) -> tuple[float, float]:
        """Return the screen x of the leftmost and rightmost LIVING invader edges.

        Using living invaders (not the original grid) means the fleet still
        travels to the true edge after its outer columns are destroyed.
        """
        lefts = [inv.home_x for inv in self.invaders]
        rights = [inv.home_x + inv.rect.width for inv in self.invaders]
        return min(lefts) + self.offset_x, max(rights) + self.offset_x

    def reached_bottom(self, y_limit: int) -> bool:
        """Return True if any invader has reached y_limit (the player's row)."""
        return any(inv.rect.bottom >= y_limit for inv in self.invaders)

    # Per-frame update
    def update(self, dt: float, enemy_bullets: pygame.sprite.Group) -> None:
        """Move the fleet, bounce at the edges, animate and maybe fire.

        dt: seconds since the last frame.
        enemy_bullets: the shared group owned by Game; new bullets go in here.
        """
        if self.alive_count() == 0:
            return
        self._move(dt)
        self._animate(dt)
        self._try_fire(dt, enemy_bullets)

    def _move(self, dt: float) -> None:
        """Move sideways; at an edge, snap to it, reverse and drop."""
        dx = self.current_speed() * dt * self.direction
        left, right = self.living_bounds()
        min_x = settings.FLEET_EDGE_MARGIN
        max_x = settings.SCREEN_WIDTH - settings.FLEET_EDGE_MARGIN

        if right + dx > max_x: # would cross the right edge
            self.offset_x += max_x - right # snap exactly to the edge
            self._bounce()
        elif left + dx < min_x: # would cross the left edge
            self.offset_x += min_x - left
            self._bounce()
        else:
            self.offset_x += dx

        for inv in self.invaders:
            inv.place(self.offset_x, self.offset_y)

    def _bounce(self) -> None:
        """Reverse direction and step the whole fleet down."""
        self.direction *= -1
        self.offset_y += settings.FLEET_DROP

    def _animate(self, dt: float) -> None:
        """Flap the invaders; the faster the fleet, the faster they flap."""
        self.anim_timer += dt
        interval = max(0.1, 20 / self.current_speed())
        if self.anim_timer >= interval:
            self.anim_timer = 0.0
            for inv in self.invaders:
                inv.animate()

    def _next_fire_delay(self) -> float:
        """Return a random number of seconds until the next shot."""
        return self.rng.uniform(settings.FLEET_FIRE_MIN, settings.FLEET_FIRE_MAX)

    def _try_fire(self, dt: float, enemy_bullets: pygame.sprite.Group) -> None:
        """When the timer runs out, a random shooter fires (if under the cap)."""
        self.fire_timer -= dt
        if self.fire_timer > 0:
            return
        self.fire_timer = self._next_fire_delay()
        if len(enemy_bullets) >= settings.INVADER_BULLET_MAX:
            return
        candidates = self.shooters()
        if not candidates:
            return
        shooter = self.rng.choice(candidates)
        enemy_bullets.add(InvaderBullet(shooter.rect.centerx, shooter.rect.bottom))

    # Callbacks and drawing
    def on_invader_destroyed(self, invader: Invader) -> None:
        """Callback from collisions.py: remove the invader from the grid.

        Safe to call twice for the same invader.
        """
        if self.grid[invader.row][invader.col] is invader:
            self.grid[invader.row][invader.col] = None
        invader.kill() # removes it from every group

    def draw(self, surface: pygame.Surface) -> None:
        """Draw every living invader."""
        self.invaders.draw(surface)
