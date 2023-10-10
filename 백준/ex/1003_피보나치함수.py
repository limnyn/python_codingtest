# https://www.acmicpc.net/problem/1003

for i in range(int(input())):
    dp = [[1, 0], [0, 1]]
    n = int(input())
    if n < 2:
        print(dp[n][0], dp[n][1])
    else:
        for _ in range(2, n + 1):
            dp.append([dp[-1][0] + dp[-2][0], dp[-1][1] + dp[-2][1]])
        print(dp[-1][0], dp[-1][1])
