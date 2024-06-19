# https://www.acmicpc.net/problem/7579
'''
[문제]
    M 바이트 이상의 메모리를 확보할 때, 최소의 비용 C인 경우

[입력]
    1 <= N <= 100
    1 <= M <= 10,000,000
    0 <= c1,...,cN <= 100

[접근]
    M 바이트 이상인 경우 중 최소 비용 C
    -> 특정한 앱을 선택했을 때의 최소 비용 C
    -> Knapsack의 W 이하 중 최대 비용 V 와 유사하게 느껴진다
    따라서 knapsack을 응용해보자
    
    문제 조건을 보면 C가 작은 것을 알 수 있다.
    최대 크기가 주어졌을 때 N = 100, C =  100*100
    따라서 10000 * 100 연산을 통해 한번에 구할 수 있다

[구현]
    1. C의 합에 대해서 각 C일때의 최대 메모리를 구한다.
        -> DP를 사용
    2. M 이상의 메모리 중 최소 C를 구한다.
'''
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    memories = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))
    c_sum = sum(costs)
    dp = [[0] * (c_sum + 1) for _ in range(n+1)]
    
    for r in range(1,n+1):
        for c in range(c_sum + 1):
            if c >= costs[r]:
                dp[r][c] = max(dp[r-1][c - costs[r]]+memories[r], dp[r][c])
            dp[r][c] = max(dp[r-1][c], dp[r][c])

    for i in range(c_sum + 1):
        if dp[-1][i] >= m:
            print(i)
            break


