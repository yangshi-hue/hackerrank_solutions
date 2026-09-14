def migratoryBirds(arr):
    count = {}
    for bird in arr:
        if bird in count:
            count[bird] += 1
        else:
            count[bird] = 1
    max_count = 0
    answer = 0
    for bird in count:
        if count[bird] > max_count:
            max_count = count[bird]
            answer = bird
        elif count[bird] == max_count and bird < answer:
            answer = bird
    return answer
