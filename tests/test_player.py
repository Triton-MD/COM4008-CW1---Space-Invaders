"""Tests for R2: game/player/ (Player).

Organise tests as normal, boundary and failure/edge cases. Each test name
should appear in the wiki's requirements traceability table.
"""

import importlib


def test_module_imports():
    """Placeholder so the suite runs from day one; keep it as a smoke test."""
    importlib.import_module("game.player.player")


# TODO normal:   holding fire for 1 s gives the expected number of shots
# TODO normal:   a hit player loses one life and respawns
# TODO boundary: fire pressed exactly at cooldown end
# TODO boundary: losing the last life moves to game over
# TODO failure:  bullets leaving the screen are removed; group size does not grow forever
# TODO failure:  a second hit during invulnerability does nothing
