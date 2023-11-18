# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
for t_c in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(f'# {t_c} {max(dp)}')
            