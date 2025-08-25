# https://www.acmicpc.net/problem/14267

"""
직속상사에 대해서 그래프를 만들고, 이 그래프 대로 칭찬을 전파한다.
다만 반복되는 경우가 있으니, 내 순서일 때 부모를 탐색해가며 dp 방식으로 처리한다.

직속 상사의 번호가 자신의 번호보다 작기 때문에, 작은 순서대로 탐색하면 반복 연산을 생략할 수 있다.
"""

import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    manager = [0] + list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    
    commend = [0] * (n + 1)
    for _ in range(m):
        worker, score = map(int, input().split())
        commend[worker] += score
    
    for i in range(2, n+1):
        worker = i
        dp[worker] = dp[manager[worker]] + commend[worker]
    
    for i in range(1, n + 1):
        print(dp[i], end=" ")
        
        
