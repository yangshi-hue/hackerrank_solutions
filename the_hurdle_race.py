def hurdleRace(k, height):
    tallest = max(height)

    if tallest > k:
        return tallest - k
    else:
        return 0