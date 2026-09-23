def angryProfessor(k, a):
    on_time = 0

    for student in a:
        if student <= 0:
            on_time += 1

    if on_time < k:
        return "YES"
    else:
        return "NO"