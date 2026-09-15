def pageCount(n,p):
    from_back = p //2
    from_front = n//2 - p//2
    return min(from_back, from_front)