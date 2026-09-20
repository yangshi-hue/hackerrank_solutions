def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)

    result = []

    for score in player:
        left = 0
        right = len(ranked)

        while left < right:
            mid = (left + right) // 2

            if ranked[mid] <= score:
                right = mid
            else:
                left = mid + 1

        result.append(left + 1)

    return result