def birthday(d, m, s): #the d = day of ron's birthday, m = month, s = integers 
    count = 0

    for i in range (len(s) - m+1): #moving through chocolate bar
        segment = s[i:i + m] #taking m consecutive element
        if sum(segment) ==d: #comparing segment with ron's birth day
            count += 1
    return count 

