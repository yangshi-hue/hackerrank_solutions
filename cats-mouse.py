def CatAndMouse(x, y , z):
    distance_a = (x-y)
    distance_b = (y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_a > distance_b:
        return "Cat B"
    else:
        return "Mouse"