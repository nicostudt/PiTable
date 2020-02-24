axis = {
    0: "x",
    1: "y"
}

buttons = {
    0: "X",
    1: "A",
    2: "B",
    3: "Y",
    4: "SHOULDER_L",
    5: "SHOULDER_R",
    9: "START",
    8: "SELECT"
}


def getButton(id):
    try:
        return buttons[id]
    except:
        return id


def getAxis(id):
    return axis[id]


def getValue(value):
    return max(-1, min(1, value))
