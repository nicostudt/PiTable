import games.tommy_wild.colors as colors


class Fog():
    def __init__(self, color, minAlpha):
        self.color = color
        self.minAlpha = minAlpha

    def getColor(self, colorIn, playerPos, targetPos, sight):
        # Light up sky plus part of ground
        if targetPos.y < 11:
            return colorIn
        else:
            dist = playerPos.dist(targetPos)
            alpha = self.getAlpha(dist, sight)

        return colors.interpolateColor(self.color, colorIn, alpha)

    def getAlpha(self, dist, sight):
        if dist <= sight:
            return 1

        sight2 = sight * 3

        if dist >= sight2:
            return self.minAlpha
        else:
            r = (dist - sight) / (sight2 - sight)
            return (1 - r) + self.minAlpha * r
