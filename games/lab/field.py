
def getNeights(pos, size):
    neights = []

    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        newPos = pos.clone()
        newPos.add(dx, dy)

        if inside(newPos, size):
            neights.append(newPos)

    return neights

def inside(pos, size):
    return 0 <= pos.x < size[0] and 0 <= pos.y < size[1]