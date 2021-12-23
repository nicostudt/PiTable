#!/usr/bin/python

import sys
import pygame
import signal
import engine.joystick as joystick
import time


keyMapping = {
    # Gamepad 1 emulation
    pygame.K_w:         pygame.event.Event(7, joy=0, value=-1, axis=1),
    pygame.K_s:         pygame.event.Event(7, joy=0, value=1, axis=1),
    pygame.K_a:         pygame.event.Event(7, joy=0, value=-1, axis=0),
    pygame.K_d:         pygame.event.Event(7, joy=0, value=1, axis=0),
    -pygame.K_w:        pygame.event.Event(7, joy=0, value=0, axis=1),
    -pygame.K_s:        pygame.event.Event(7, joy=0, value=0, axis=1),
    -pygame.K_a:        pygame.event.Event(7, joy=0, value=0, axis=0),
    -pygame.K_d:        pygame.event.Event(7, joy=0, value=0, axis=0),

    pygame.K_j:         pygame.event.Event(10, joy=0, button=0),
    pygame.K_i:         pygame.event.Event(10, joy=0, button=3),
    pygame.K_o:         pygame.event.Event(10, joy=0, button=1),
    pygame.K_k:         pygame.event.Event(10, joy=0, button=2),
    pygame.K_BACKSPACE: pygame.event.Event(10, joy=0, button=8),
    pygame.K_RETURN:    pygame.event.Event(10, joy=0, button=9),
    -pygame.K_j:         pygame.event.Event(11, joy=0, button=0),
    -pygame.K_i:         pygame.event.Event(11, joy=0, button=3),
    -pygame.K_o:         pygame.event.Event(11, joy=0, button=1),
    -pygame.K_k:         pygame.event.Event(11, joy=0, button=2),
    -pygame.K_BACKSPACE: pygame.event.Event(11, joy=0, button=8),
    -pygame.K_RETURN:    pygame.event.Event(11, joy=0, button=9),

    # Gamepad 2 emulation
    pygame.K_UP:        pygame.event.Event(7, joy=1, value=-1, axis=1),
    pygame.K_DOWN:      pygame.event.Event(7, joy=1, value=1, axis=1),
    pygame.K_LEFT:      pygame.event.Event(7, joy=1, value=-1, axis=0),
    pygame.K_RIGHT:     pygame.event.Event(7, joy=1, value=1, axis=0),
    -pygame.K_UP:       pygame.event.Event(7, joy=1, value=0, axis=1),
    -pygame.K_DOWN:     pygame.event.Event(7, joy=1, value=0, axis=1),
    -pygame.K_LEFT:     pygame.event.Event(7, joy=1, value=0, axis=0),
    -pygame.K_RIGHT:    pygame.event.Event(7, joy=1, value=0, axis=0),

    pygame.K_KP4:         pygame.event.Event(10, joy=1, button=0),
    pygame.K_KP8:         pygame.event.Event(10, joy=1, button=3),
    pygame.K_KP6:         pygame.event.Event(10, joy=1, button=1),
    pygame.K_KP2:         pygame.event.Event(10, joy=1, button=2),
    pygame.K_KP7:         pygame.event.Event(10, joy=1, button=8),
    pygame.K_KP9:         pygame.event.Event(10, joy=1, button=9),
    -pygame.K_KP4:         pygame.event.Event(11, joy=1, button=0),
    -pygame.K_KP8:         pygame.event.Event(11, joy=1, button=3),
    -pygame.K_KP6:         pygame.event.Event(11, joy=1, button=1),
    -pygame.K_KP2:         pygame.event.Event(11, joy=1, button=2),
    -pygame.K_KP7:         pygame.event.Event(11, joy=1, button=8),
    -pygame.K_KP9:         pygame.event.Event(11, joy=1, button=9)
}


class Engine(object):

    def __init__(self, home, screensaver, display):
        self.home = home
        self.home.setEngine(self)

        self.screensaver = screensaver
        self.screensaverTime = 60 * 30

        self.display = display
        self.fixStep = True

    def init(self):
        pygame.init()

        # Init Display
        self.display.init()

        # Setup clock
        self.clock = pygame.time.Clock()

        # Create a list of available joysticks and initialize them.
        joys = [pygame.joystick.Joystick(
            x) for x in range(pygame.joystick.get_count())]
        for joy in joys:
            joy.init()

        self.screensaver.initialize()
        self.setScreensave(False)

    def setScreensave(self, flag):
        print("Set screensave: " + str(flag))
        if flag:
            self.screensave = True
            self.setGame(self.screensaver)
        else:
            self.setGame(self.home)
            self.screensave = False
            self.lastAction = time.time()

    def keyboardInterruptHandler(self, signal, frame):
        print("KeyboardInterrupt (ID: {}). Cleaning up...".format(signal))
        self.exit()

    def setGame(self, game):
        self.game = game

        # Init game
        self.game.initialize()

    def run(self):
        if self.game is None:
            print("No Game inserted! Shutdown the engines")
            return

        elif self.display is None:
            print("No Display found! Shutdown the engines")
            return

        signal.signal(signal.SIGINT, self.keyboardInterruptHandler)

        self.running = True
        dt = self.clock.get_time()

        # Start game loop
        while self.running:

            # Inputs for game
            self.computeInputs()

            if time.time() - self.lastAction >= self.screensaverTime \
                    and not self.screensave:
                self.setScreensave(True)

            # Update game
            if self.fixStep:
                dt = 1.0 / self.game.getFps()
            else:
                dt = self.clock.get_time() / 1000.0

            self.game.update(dt)

            # Render game
            self.game.render(self.display)

            # Keep frames per second
            self.clock.tick(self.game.getFps())

        self.exit()

    def computeInputs(self):
        events = pygame.event.get()

        if len(events) > 0:
            self.lastAction = time.time()

            if self.screensave:
                self.setScreensave(False)
                return

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.JOYBUTTONDOWN:
                player = event.joy
                button = joystick.getButton(event.button)

                # Check if boss want home
                if player == 0 and button == "SELECT" \
                        and self.game.getName() != "Home":
                    self.setGame(self.home)
                else:
                    self.game.onButtonDown(player, button)

            elif event.type == pygame.JOYBUTTONUP:
                player = event.joy
                button = joystick.getButton(event.button)

                self.game.onButtonUp(player, button)

            elif event.type == pygame.JOYAXISMOTION:
                player = event.joy
                axis = joystick.getAxis(event.axis)
                value = joystick.getValue(event.value)

                self.game.onAxisMotion(player, axis, value)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                elif event.key in keyMapping:
                    pygame.event.post(keyMapping[event.key])

            elif event.type == pygame.KEYUP:
                if -event.key in keyMapping:
                    pygame.event.post(keyMapping[-event.key])

    def exit(self):
        self.display.fill([0, 0, 0])
        self.display.show()
        # Quit game and close window
        self.game.quit()
        pygame.quit()
        sys.exit(0)
