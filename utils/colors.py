hex = {
    "black":                "#000000",
    "white":                "#FFFFFF",
    "red":                  "#FF0000",
    "green":                "#00FF00",
    "blue":                 "#0000FF",
    "woodbrown":            "#caa472",
    "material_black":       "#2D3027",
    "material_lightgray":   "#95a5a6",
    "material_darkgray":    "#424242",
    "material_gray":        "#7f8c8d",
    "material_white":       "#ecf0f1",
    "material_red":         "#e74c3c",
    "material_green":       "#2ecc71",
    "material_darkgreen":   "#1b5e20",
    "material_blue":        "#3498db",
    "material_darkblue":    "#0D47A1",
    "material_brown":       "#795548",
    "material_darkbrown":   "#4E342E",
    "material_darkorange":  "#f57f17",
    "material_darkpurple":  "673ab7",#"#9c27b0",
    "material_darklime":    "#9e9d24",
    "material_gold":        "#fdd835",
}


def getColor(key):
    if key not in hex:
        return [0, 0, 0]

    return hexToRgb(hex[key])


def interpolateColor(fromColor, toColor, alpha):
    if alpha <= 0:
        return fromColor

    elif alpha >= 1:
        return toColor

    else:
        return [int(fromColor[i] + (toColor[i] - fromColor[i]) * alpha)
                    for i in range(3)]

def interpolateBetween(colors, alpha):
    if alpha <= colors[0][1]:
        return colors[0][0]

    elif alpha >= colors[-1][1]:
        return colors[-1][0]

    for i in range(len(colors) -1):
        fromC = colors[i]
        toC = colors[i+1]

        if alpha < toC[1]:
            a = (alpha - fromC[1]) / (toC[1] -fromC[1])
            return [int(fromC[0][i] + (toC[0][i] - fromC[0][i]) * a)
                        for i in range(3)]

def hexToRgb(value):
    value = value.lstrip('#')
    lv = len(value)
    lv3 = lv // 3

    return [int(value[i:i + lv3], 16) for i in range(0, lv, lv3)]
