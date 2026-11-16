"""Tests for R1: game/fleet/ (Invader and Fleet).

Organised as normal, boundary and failure/edge cases. Each test name
appears in the wiki's requirements traceability table.
"""

import random
import pygame
import pytest

import settings
from game.fleet.fleet import Fleet
from game.fleet.invader import Invader
from game.projectiles import InvaderBullet, PlayerBullet


@pytest.fixture
def fleet():
    # Seeded so random firing is the same every run
    return Fleet(rng=random.Random(42))


def kill_column(fleet, col):
    # Helper: destroy every invader in one column
    for row in range(len(fleet.grid)):
        inv = fleet.grid[row][col]
        if inv is not None:
            fleet.on_invader_destroyed(inv)


def run_until_reverse(fleet, max_frames):
    # Helper: step the fleet at 60 FPS until it turns round
    group = pygame.sprite.Group()
    for _ in range(max_frames):
        fleet.update(1 / 60, group)
        group.empty()  # ignore bullets here
        if fleet.direction == -1:
            break


# Normal cases

def test_fleet_has_55_invaders_of_three_kinds(fleet):
    # 5 x 11 grid, all three kinds, right kind in each row
    assert fleet.alive_count() == 55
    assert {inv.kind for inv in fleet.invaders} == {0, 1, 2}
    for row, kind in enumerate(settings.FLEET_LAYOUT):
        assert all(inv.kind == kind for inv in fleet.grid[row])


def test_points_match_kind(fleet):
    # Top row is worth most, bottom row least
    assert fleet.grid[0][0].points == 30
    assert fleet.grid[4][0].points == 10


def test_fleet_moves_right_at_start(fleet):
    x = fleet.grid[0][0].rect.x
    fleet.update(0.5, pygame.sprite.Group())
    assert fleet.grid[0][0].rect.x > x


def test_speed_rises_after_each_kill(fleet):
    before = fleet.current_speed()
    fleet.on_invader_destroyed(fleet.grid[0][0])
    assert fleet.current_speed() > before


def test_only_bottom_invader_in_each_column_fires(fleet):
    # One shooter per column, all from the bottom row
    shooters = fleet.shooters()
    assert len(shooters) == settings.FLEET_COLS
    assert all(inv.row == len(fleet.grid) - 1 for inv in shooters)


def test_invader_bullet_moves_down_and_is_removed_off_screen():
    group = pygame.sprite.Group(InvaderBullet(100, settings.SCREEN_HEIGHT - 5))
    bullet = next(iter(group))
    y = bullet.rect.y
    group.update(0.01)
    assert bullet.rect.y > y # moved down
    group.update(1.0)
    assert len(group) == 0 # killed once off screen


# Boundary cases

def test_reverses_and_drops_at_right_edge(fleet):
    y = fleet.grid[0][0].rect.y
    run_until_reverse(fleet, 2000)
    _, right = fleet.living_bounds()
    assert fleet.direction == -1
    # Turned exactly at the edge and dropped one step
    assert right == pytest.approx(settings.SCREEN_WIDTH - settings.FLEET_EDGE_MARGIN)
    assert fleet.grid[0][0].rect.y == y + settings.FLEET_DROP


def test_speed_capped_with_one_invader_left(fleet):
    for inv in list(fleet.invaders)[1:]:
        fleet.on_invader_destroyed(inv)
    assert fleet.alive_count() == 1
    # Formula alone would give 1650 px/s
    assert fleet.current_speed() == settings.FLEET_MAX_SPEED


def test_column_with_one_invader_left_still_fires(fleet):
    # Leave only the top invader in column 3
    for row in range(1, len(fleet.grid)):
        fleet.on_invader_destroyed(fleet.grid[row][3])
    assert fleet.grid[0][3] in fleet.shooters()


def test_reached_bottom(fleet):
    assert not fleet.reached_bottom(settings.SCREEN_HEIGHT - 50)
    # Push the fleet far down
    fleet.offset_y = 1000
    for inv in fleet.invaders:
        inv.place(fleet.offset_x, fleet.offset_y)
    assert fleet.reached_bottom(settings.SCREEN_HEIGHT - 50)


    # Failure / edge cases
def test_cleared_outer_columns_fleet_reaches_true_edge(fleet):
    # Common bug: bouncing early once the outer columns are gone
    kill_column(fleet, 9)
    kill_column(fleet, 10)
    run_until_reverse(fleet, 3000)
    rightmost = max(inv.rect.right for inv in fleet.invaders)
    assert rightmost == settings.SCREEN_WIDTH - settings.FLEET_EDGE_MARGIN


def test_zero_invaders_no_division_by_zero(fleet):
    # list() copy: don't change a group while looping over it
    for inv in list(fleet.invaders):
        fleet.on_invader_destroyed(inv)
    assert fleet.current_speed() == 0
    assert fleet.shooters() == []
    fleet.update(1 / 60, pygame.sprite.Group()) # must not crash


def test_seeded_rng_gives_same_shots():
    def shots(seed):
        # Run 10 seconds and record where each bullet was fired
        f = Fleet(rng=random.Random(seed))
        g = pygame.sprite.Group()
        xs = []
        for _ in range(600):
            f.update(1 / 60, g)
            xs.extend(b.rect.centerx for b in g)
            g.empty()
        return xs
    assert shots(1) == shots(1) # same seed, same shots
    assert len(shots(1)) > 0 # and it does fire


def test_enemy_bullet_cap_respected(fleet):
    # Bullets are never removed here, so the cap is the only limit
    g = pygame.sprite.Group()
    for _ in range(600):
        fleet.update(1 / 60, g)
    assert len(g) <= settings.INVADER_BULLET_MAX


def test_destroying_same_invader_twice_is_safe(fleet):
    inv = fleet.grid[2][2]
    fleet.on_invader_destroyed(inv)
    fleet.on_invader_destroyed(inv)
    assert fleet.alive_count() == 54


def test_unknown_kind_rejected():
    with pytest.raises(ValueError):
        Invader(7, 0, 0, 0, 0)


def test_groupcollide_two_bullets_score_once(fleet):
    # Two bullets hit the same invader in one frame
    target = fleet.grid[4][5]
    bullets = pygame.sprite.Group(
        PlayerBullet(target.rect.centerx, target.rect.top),
        PlayerBullet(target.rect.centerx + 2, target.rect.top),
    )
    hits = pygame.sprite.groupcollide(fleet.invaders, bullets, False, True)
    score = 0
    for inv in hits:
        score += inv.points
        fleet.on_invader_destroyed(inv)
    assert score == 10 # not 20
    assert fleet.alive_count() == 54


# TODO normal:   fleet has 55 invaders of 3 kinds in the right rows
# TODO normal:   speed rises after each kill
# TODO normal:   only the bottom invader in a column fires
# TODO boundary: fleet reverses exactly when the rightmost living invader touches the edge
# TODO boundary: last invader reaches the capped max speed, not infinity
# TODO boundary: a column with one invader left still fires
# TODO failure:  clearing the outer columns, the fleet still travels to the true edge
# TODO failure:  zero invaders alive gives no division by zero
# TODO failure:  seeded random gives the same shots every run; enemy bullet cap respected
