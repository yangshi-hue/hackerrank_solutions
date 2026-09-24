def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reverse_day = int(str(day)[::-1]) #reverse the days
        difference = abs(day - reverse_day)
        if difference % k == 0:
            count+=1
    return count