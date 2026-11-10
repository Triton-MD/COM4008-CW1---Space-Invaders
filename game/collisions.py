"""The one collision step, run once per frame in a fixed order.

SHARED FILE: Write the order on the integration wiki page and explain why.

Order:
1. Bullets vs barriers    (first, so barriers actually protect)
2. Player bullets vs invaders
3. Invader bullets vs player
4. Invaders vs barriers   (descending invaders erase what they overlap)

Callbacks, not reach-ins: this module calls fleet.on_invader_destroyed(invader)
and player.on_hit(); it does not edit their internals directly.
"""


def resolve(game):
    """Run every collision check for this frame, in the order above.

    TODO: call the helper functions below in order. Return or apply the
    score gained this frame.
    """
    pass


def bullets_vs_barriers(bullet_groups, barriers):
    """Remove bullets that hit a barrier and erode the barrier at that point."""
    pass


def player_bullets_vs_invaders(player_bullets, fleet):
    """Kill hit invaders, tell the fleet, and return the points scored."""
    pass


def invader_bullets_vs_player(enemy_bullets, player):
    """If an invader bullet hits the player, call player.on_hit()."""
    pass


def invaders_vs_barriers(fleet, barriers):
    """Erase the parts of barriers that invaders overlap."""
    pass
