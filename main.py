#!/usr/bin/python

from engine.engine import Engine
import games

if __name__ == "__main__":
    # Init Game
    game = games.Home()

    # Check if running on pi
    try:
        import RPi.GPIO as gpio

        from display.stripDisplay import StripDisplay
        display = StripDisplay()

    except (ImportError, RuntimeError):
        from display.pygamePixelDisplay import PygamePixelDisplay
        display = PygamePixelDisplay(caption=game.getName())

    screensaver = games.Anim()

    # Init Engine
    engine = Engine(game, screensaver, display)
    engine.init()
    engine.run()
