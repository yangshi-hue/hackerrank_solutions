def pickingNumbers(a):
    max_length = 0

    for num in a:
        length = a.count(num) + a.count(num + 1)
        max_length = max(max_length, length)

    return max_length