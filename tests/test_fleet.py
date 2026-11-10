"""Tests for R1: game/fleet/ (Invader and Fleet).

Organise tests as normal, boundary and failure/edge cases. Each test name
should appear in the wiki's requirements traceability table.
"""

import importlib


def test_module_imports():
    """Placeholder so the suite runs from day one; keep it as a smoke test."""
    importlib.import_module("game.fleet.fleet")


# TODO normal:   fleet has 55 invaders of 3 kinds in the right rows
# TODO normal:   speed rises after each kill
# TODO normal:   only the bottom invader in a column fires
# TODO boundary: fleet reverses exactly when the rightmost living invader touches the edge
# TODO boundary: last invader reaches the capped max speed, not infinity
# TODO boundary: a column with one invader left still fires
# TODO failure:  clearing the outer columns, the fleet still travels to the true edge
# TODO failure:  zero invaders alive gives no division by zero
# TODO failure:  seeded random gives the same shots every run; enemy bullet cap respected
