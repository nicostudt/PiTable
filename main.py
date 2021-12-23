#!/usr/bin/python

from engine.engine import Engine
import games


def main():
    # Init first "game" on screen
    print("Start")
    game = games.Home()

    # Check if running on pi
    try:
        import RPi.GwwPIO as gpio

        from display.stripDisplay import StripDisplay
        display = StripDisplay()

    except (ImportError, RuntimeError):
        from display.pygamePixelDisplay import PygamePixelDisplay
        display = PygamePixelDisplay(caption="PiTable Emulator",
                                     gridSize=[16, 16],
                                     width=1000,
                                     height=1000,
                                     space=2)

    screensaver = games.Anim()

    # Init Engine
    engine = Engine(game, screensaver, display)
    engine.init()
    engine.run()


if __name__ == "__main__":
    main()
