# https://www.acmicpc.net/problem/2579

n = int(input())


"""
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
 즉 한 계단을 밟으면서 이어서 다음 계단이나. 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안된다.
 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
"""

nums = [0]*301
dp = [0]*301

for i in range(n):
    nums[i+1] = int(input())
dp[1] = nums[1]
dp[2] = nums[1] + nums[2]
dp[3] = max(nums[1] + nums[3], nums[2] + nums[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2], nums[i-1]+dp[i-3])+nums[i]



print(dp[n])