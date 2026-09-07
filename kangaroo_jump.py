def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    position_difference = x2-x1
    speed_difference = v1-v2
    if position_difference % speed_difference == 0:
        jumps = position_difference // speed_difference
    if jumps >= 0:
        return "YES"
    return "NO"