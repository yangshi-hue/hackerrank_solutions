def sockMerchant(n, ar):
    count = {}
    pairs = 0

    for sock in ar:
        if sock in count :
            count[sock]+=1
        else:
            count[sock] =1
    for color in count:
        pairs += count[color]//2
    return pairs
