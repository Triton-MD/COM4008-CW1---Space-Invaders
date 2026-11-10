"""Tests for R3: game/barriers/ (Barrier and barrier_row).

Organise tests as normal, boundary and failure/edge cases. Each test name
should appear in the wiki's requirements traceability table.
"""

import importlib


def test_module_imports():
    """Placeholder so the suite runs from day one; keep it as a smoke test."""
    importlib.import_module("game.barriers.barrier")


# TODO normal:   a player bullet removes part of a barrier
# TODO normal:   an invader bullet erodes from the top
# TODO normal:   four barriers are evenly spaced across the screen width
# TODO boundary: a hit on the very edge pixel of a barrier
# TODO boundary: a fully destroyed barrier causes no more collisions
# TODO failure:  a bullet through an already destroyed gap passes through
# TODO failure:  invaders overlapping a barrier erase it
