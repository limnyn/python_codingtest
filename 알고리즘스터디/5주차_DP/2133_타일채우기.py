n = int(input())

dp = [0]*(31)
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    # print(i)
    dp[i] = dp[i-2] * dp[2] + 4
# print(dp)
print(dp[n])

# print(dp[n])

