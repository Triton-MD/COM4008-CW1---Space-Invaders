"""Entry point for the game.

Run from the project root with:  python main.py

This file stays tiny on purpose (about 10 lines). All it does is create the
Game object and start its main loop. Everything else lives in the game/ package,
so tests can import the game without opening a window.
"""

# Full-path imports (game.game) work the same here and in tests/, as long as
# you always run from the project root.
from game.game import Game


def main():
    """Create the Game and run it until the player quits."""
    # TODO: optionally read command-line flags here (for example --debug to
    # draw hitboxes and show FPS / invader count / fleet speed).
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
