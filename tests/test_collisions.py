"""Tests for the shared collision step: game/collisions.py.

Organise tests as normal, boundary and failure/edge cases. Each test name
should appear in the wiki's requirements traceability table.
"""

import importlib


def test_module_imports():
    """Placeholder so the suite runs from day one; keep it as a smoke test."""
    importlib.import_module("game.collisions")


# TODO normal:   a bullet hitting an invader removes both and adds score
# TODO normal:   bullets vs barriers is checked before bullets vs invaders
# TODO boundary: a bullet clipping the corner of an invader
# TODO failure:  two bullets hitting the same invader in one frame score once
