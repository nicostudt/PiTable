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
    "material_blue":        "#3498db",
    "material_brown":       "#795548",
    "material_darkbrown":   "#4E342E",

}


def getColor(key):
    if key not in hex:
        return [0, 0, 0]

    return hexToRgb(hex[key])


def interpolateColor(fromColor, toColor, alpha):
    if alpha == 0:
        return fromColor

    elif alpha == 1:
        return toColor

    else:
        newColor = [int(fromColor[i] + (toColor[i] - fromColor[i]) * alpha)
                    for i in range(3)]
        return newColor


def hexToRgb(value):
    value = value.lstrip('#')
    lv = len(value)
    lv3 = lv // 3

    return [int(value[i:i + lv3], 16) for i in range(0, lv, lv3)]
