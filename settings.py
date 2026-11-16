"""Every tweakable number in one place.

SHARED FILE: everyone on the team edits this, so changes go through a reviewed PR.

Rule: no module should hard-code a screen size, speed, colour or count. Import it
from here instead, e.g.  from settings import SCREEN_WIDTH
The values below are starting points; tune them as you build and record why on
the wiki if a value is a design decision (for example the speed-up curve).
"""

# --- Window -------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60                      # clock.tick(FPS); dt = ms_since_last_frame / 1000
TITLE = "Space Defenders"     # use your own game name, not the arcade original

# --- Colours (R, G, B) --------------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --- R1: Invader fleet --------------------------------------------------
FLEET_ROWS = 5
FLEET_COLS = 11
FLEET_LAYOUT = [2, 1, 1, 0, 0] # row index -> invader kind
INVADER_WIDTH = 32
INVADER_HEIGHT = 24
FLEET_START_X = 80 # left edge of column 0 at the start of a wave
FLEET_START_Y = 80 # top edge of row 0
FLEET_H_SPACING = 48 # distance between column left edges
FLEET_V_SPACING = 40 # distance between row top edges
FLEET_EDGE_MARGIN = 10 # gap kept from the screen edge
FLEET_BASE_SPEED = 30 # px/s with all invaders alive
FLEET_MAX_SPEED = 300 # px/s cap (last invader)
FLEET_DROP = 16 # px the fleet drops at each edge
FLEET_FIRE_MIN = 0.4 # seconds between invader shots (random range)
FLEET_FIRE_MAX = 1.2
INVADER_BULLET_MAX = 3 # most invader bullets on screen at once
INVADER_POINTS = {0: 10, 1: 20, 2: 30}
# TODO (R1): base speed, drop distance, max speed cap, fire chance,
# enemy bullet cap, points per kind.

# --- R2: Player ---------------------------------------------------------
PLAYER_LIVES = 3
# TODO (R2): player speed, shot cooldown (seconds), max player bullets,
# respawn delay, invulnerability time.

# --- R3: Barriers -------------------------------------------------------
BARRIER_COUNT = 4
# TODO (R3): barrier size, vertical position, block/bite size.

# --- Projectiles (shared) -----------------------------------------------
# TODO: player bullet speed, invader bullet speed.
