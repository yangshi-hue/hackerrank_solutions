def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]

    max_count = 0
    min_count = 0

    for score in scores[1:]:
        if score > highest :
            highest = score
            max_count += 1

        if score < lowest:
            lowest = score
            min_count +=1 
    return [max_count, min_count]