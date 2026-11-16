"""One invader: its kind, points value and animation frames (R1).
 
Design choice: one Invader class plus a data table (kind -> sprite names)
rather than three subclasses, because the three kinds behave the same and
only their data differs. Points come from settings.INVADER_POINTS.
"""
 
import pygame
 
import settings
from game import assets
 
INVADER_TYPES = {
    0: {"frames": ["invader_a_1", "invader_a_2"], "colour": (0, 255, 255)},
    1: {"frames": ["invader_b_1", "invader_b_2"], "colour": (255, 0, 255)},
    2: {"frames": ["invader_c_1", "invader_c_2"], "colour": (255, 255, 0)},
}
 
 
def _load_frame(name: str, colour: tuple) -> pygame.Surface:
    """Load a frame by name, or a coloured box until the art exists."""
    try:
        return assets.image(name)
    except (NotImplementedError, FileNotFoundError, pygame.error):
        surface = pygame.Surface((settings.INVADER_WIDTH, settings.INVADER_HEIGHT))
        surface.fill(colour)
        return surface
 
 
class Invader(pygame.sprite.Sprite):
    """A single alien in the fleet."""
 
    def __init__(self, kind: int, row: int, col: int, x: float, y: float):
        """Create an invader of the given kind with its home at (x, y).
 
        row, col: its cell in fleet.grid, so the fleet can clear it on death.
        Raises ValueError for an unknown kind.
        """
        super().__init__()
        if kind not in INVADER_TYPES:
            raise ValueError(f"Unknown invader kind: {kind}")
        data = INVADER_TYPES[kind]
        self.kind = kind
        self.row = row
        self.col = col
        self.points = settings.INVADER_POINTS[kind]
        self.frames = [_load_frame(name, data["colour"]) for name in data["frames"]]
        self.frame_index = 0
        self.image = self.frames[0]
        self.home_x = x # position when the fleet offset is (0, 0)
        self.home_y = y
        self.rect = self.image.get_rect(topleft=(round(x), round(y)))
 
    def place(self, offset_x: float, offset_y: float) -> None:
        """Put the invader at its home position plus the fleet's offset."""
        self.rect.topleft = (round(self.home_x + offset_x),
                             round(self.home_y + offset_y))
 
    def animate(self) -> None:
        """Swap to the next animation frame."""
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image = self.frames[self.frame_index]
 