def interpolate(color1, color2, alpha):
    return [color1[i] + (color2[i] - color1[i]) * alpha for i in range(3)]
