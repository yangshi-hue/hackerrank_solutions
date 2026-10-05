def ViralAdvertising(n):
    people = 5
    total_likes = 0
    for day in range(n):
        likes = people // 2
        total_likes += likes
        people = likes * 3
    return total_likes