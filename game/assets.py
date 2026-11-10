"""Loads each image and sound once, by name.

This is the ONLY file that knows file paths. Everyone else asks for an asset by
name, e.g. assets.image("invader_a_1"), so moving or renaming files means
changing one place.

Asset names are lowercase with underscores and a frame number:
    assets/images/invaders/invader_a_1.png, invader_a_2.png, ...
"""

from pathlib import Path

# Project root / assets, worked out from this file's location so it works
# no matter where Python is started from.
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"
FONTS_DIR = ASSETS_DIR / "fonts"


def image(name):
    """Return the pygame Surface for the named image, loading it on first use.

    TODO: search IMAGES_DIR for f"{name}.png", load with
    pygame.image.load(...).convert_alpha(), cache it in a dict.
    """
    raise NotImplementedError


def sound(name):
    """Return the pygame Sound for the named sound, loading it on first use."""
    raise NotImplementedError


def font(name, size):
    """Return a pygame Font of the given size (fall back to the default font)."""
    raise NotImplementedError
