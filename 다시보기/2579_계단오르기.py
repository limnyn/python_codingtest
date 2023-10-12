# https://www.acmicpc.net/problem/2579

n = int(input())
dp = [0] * 301
stair = [0] * 301

for i in range(n):
    stair[i + 1] = int(input())

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])
for i in range(4, n + 1):
    dp[i] = max(stair[i - 1] + dp[i - 3], dp[i - 2]) + stair[i]

print(dp[n])
