"""Shared pytest setup: headless pygame and shared fixtures.

SDL_VIDEODRIVER=dummy lets pygame run without a window
"""

import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

# Make the project root importable, so tests can use full paths such as
# `from game.fleet.fleet import Fleet` however pytest is started.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
import pytest  


@pytest.fixture(scope="session", autouse=True)
def pygame_headless():
    """Initialise pygame once for the whole test run, then shut it down."""
    pygame.init()
    pygame.display.set_mode((1, 1))  # some calls (convert_alpha) need a display
    yield
    pygame.quit()


# TODO: add shared fixtures here, for example a seeded rng:
# @pytest.fixture
# def rng():
#     import random
#     return random.Random(42)
