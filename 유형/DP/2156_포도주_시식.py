# https://www.acmicpc.net/problem/2156

'''
n번째 잔일 때 최대인 경우
1. n번째 잔을 선택하지 않은 경우
    - n-1번째 잔을 선택한 경우가 최대값
2. n번째 잔을 선택한 경우
    2.1 n번째 잔과 n-1번째 잔을 선택한 경우
        이 경우 n, n-1번째 잔을 마시면 n-2번째 잔을 마실 수 없다. 따라서 n-3번째 잔을 선택한 경우의 최대값으로 계산
        dp[n] = wine[n] + wine[n-1] + dp[n-2]
    2.2 n번째 잔과 n-2번째 잔을 선택한 경우
        dp[n] = dp[n-2] + wine[n]
'''
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    wine = [0]
    for _ in range(n):
        wine.append(int(input()))
    
    dp = [0] * (n + 1)
    dp[1] = wine[1]

    if n >= 1:
        dp[1] = wine[1]
    if n >= 2:
        dp[2] = wine[1] + wine[2]
    # if n >= 3:
    #     dp[3] = max(wine[1] + wine[3], wine[2] + wine[3], dp[2])
        
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],
            wine[i] + wine[i - 1] + dp[i - 3],
            wine[i] + dp[i - 2]
        )
    print(dp[-1])
    
        
