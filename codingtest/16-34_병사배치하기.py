# https://www.acmicpc.net/problem/18353

# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
# https://rebro.kr/33
n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
dp = [1]* (n)
for i in range(n):

    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1) 
            
    

print(n - max(dp))

# // Answer: 5