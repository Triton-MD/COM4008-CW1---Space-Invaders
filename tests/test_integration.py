"""Integration tests: build a small game world and step it a few frames.

Organise tests as normal, boundary and failure/edge cases. Each test name
should appear in the wiki's requirements traceability table.
"""

import importlib


def test_module_imports():
    """Placeholder so the suite runs from day one; keep it as a smoke test."""
    importlib.import_module("game.game")


# TODO: bullet travels, hits, invader count drops, fleet speed rises
# TODO: invader bullet hits player -> life lost -> respawn state
# TODO: invaders reaching the player row -> game over
