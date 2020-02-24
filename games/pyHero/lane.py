
class Lane():

    def __init__(self, game, x, colour, button, player=0):
        self.game = game
        self.x = x
        self.colour = colour
        alpha = 0.5
        self.lightcolour = [self.colour[i] * alpha for i in range(3)]
        self.button = button
        self.pressed = False
        self.notes = []
        self.speed = 10
        self.fadeTimer = 0
        self.maxFadeTimer = 0.5

    def renderNotes(self, screen):
        for note in self.notes:
            screen.setPixel(self.x, int(round(note.y)), self.colour)

    def removeNote(self, note):
        self.notes.remove(note)

    def hit(self):
        if self.pressed:

            for note in self.notes:

                dist = abs(note.y - 14.5) / self.speed
                if dist < 0.5 / self.speed:
                    self.removeNote(note)
                    self.fade(self.colour)
                    return 1
                elif dist < 1.5 / self.speed:
                    self.removeNote(note)
                    self.fade(self.lightcolour)
                    return 2

        return 0

    def update(self, dt):

        for note in self.notes:
            note.move(dt * self.speed)
            if note.y > 15:
                self.game.decreaseScore(5)
                self.notes.remove(note)

        self.fadeTimer = max(0, self.fadeTimer - dt)

    def interpolate(self, colour1, colour2, alpha):
        return[colour1[i] + (colour2[i] - colour1[i]) * alpha for i in range(3)]

    def fade(self, colour):
        self.fadeColour = colour
        self.fadeTimer = self.maxFadeTimer

    def render(self, screen):

        if self.fadeTimer > 0:
            alpha = self.fadeTimer / self.maxFadeTimer
            c = self.interpolate([0, 0, 0], self.fadeColour, alpha)

            screen.setPixel(self.x, 14, c)
            screen.setPixel(self.x - 1, 13, c)
            screen.setPixel(self.x + 1, 13, c)
            screen.setPixel(self.x - 1, 15, c)
            screen.setPixel(self.x + 1, 15, c)
        # render button
        if not self.pressed:
            # screen.setPixel(self.x,14,self.colour)
            screen.setPixel(self.x, 13, self.lightcolour)
            screen.setPixel(self.x, 15, self.lightcolour)
            screen.setPixel(self.x + 1, 14, self.lightcolour)
            screen.setPixel(self.x - 1, 14, self.lightcolour)

        elif self.pressed:
            screen.setPixel(self.x, 13, self.colour)
            screen.setPixel(self.x, 15, self.colour)
            screen.setPixel(self.x + 1, 14, self.colour)
            screen.setPixel(self.x - 1, 14, self.colour)
        # render Notes
        self.renderNotes(screen)
