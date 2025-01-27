# https://www.acmicpc.net/problem/2294
"""
dp[i] = min(dp[i], dp[i - coin] + 1)
-> 해당 코인을 사용할 때랑 사용하지 않을 때 중 적게 사용하는 경우가 정답.
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    
    coin_input = [int(input()) for _ in range(n)]
    
    # dp[i] = 금액 i를 만들기 위한 최소 동전 개수
    dp = [float("inf")] * (k + 1)

    coins = []
    for coin in coin_input: # k보다 큰 코인은 사용하지 않음
        if coin <= k:
            dp[coin] = 1 # 각 금액별 필요한 동전수 갱신
            coins.append(coin)

    for coin in coins:
        for i in range(1, k + 1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    
    if dp[k] == float("inf"):
        print(-1)
    else:
        print(dp[k])

if __name__ == "__main__":
    main()