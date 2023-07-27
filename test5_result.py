def countWaysToColorHouses(n):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(n)]
    for c1 in range(1, 4):
        for c2 in range(1, 4):
            if c1 != c2:
                dp[1][c1][c2] = 1

    mod = 10 ** 9 + 7
    for i in range(2, n // 2 + 1):
        for c1 in range(1, 4):
            for c2 in range(1, 4):
                for c3 in range(1, 4):
                    for c4 in range(1, 4):
                        if c1 != c4 and c2 != c3 and c1 != c2 and c3 != c4:
                            dp[i][c3][c4] += dp[i - 1][c1][c2]
                            dp[i][c3][c4] %= mod

    ans = 0
    for c1 in range(1, 4):
        for c2 in range(1, 4):
            ans = (ans + dp[n // 2][c1][c2]) % mod
    return ans