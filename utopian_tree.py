def utopianTree(n):
    height = 1

    for i in range(n):
        if i % 2 == 0:      # Spring
            height *= 2
        else:               # Summer
            height += 1

    return height