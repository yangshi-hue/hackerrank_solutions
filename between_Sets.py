def getTotalX(a,b):
    count = 0
    for x in range(max(a), min(b)+1):
        first_condition = all(x % num == 0 for num in a)
        second_condition = all(num % x == 0 for num in b)

        if first_condition and second_condition:
            count += 1
    return count 