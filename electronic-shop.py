def getMoney(keyboards, drives, b):
    best = -1
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard+ drive

            if total <= best:
                best = max(best, total)
    return best