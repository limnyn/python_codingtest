# https://www.acmicpc.net/problem/1577

'''
[접근]
(0, 0)에서 (N, M)까지 가는 경로에 대해
(i,j)까지 가는 길 = (i-1, j) + (i, j+1)

따라서 DP 접근 가능

[주의사항]
특정 좌표에 대해 접근 불가능한것이 아닌, 특정 간선(도로)가 접근 불가능
차단된 도로의 길이는 항상 1
따라서 a,b,c,d에 대해 a+c+b+d 는 항상 홀수 
- 항상 (a,c가 같거나 b,d가 같음)

blocked 배열을 2*m*2*n길이로 만들어서 [a+c][b+d]배열에 대해 a+c+b+d가 홀수인 경우
해당 방향이 막혀있는것

'''

import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    # 입력 처리
    n, m = map(int, input().split())
    k = int(input())

    # DP 배열 및 공사 중인 도로 정보 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    blocked = [[0] * (201) for _ in range(201)]
    
    # 공사 중인 도로 입력 처리
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        if (a, b) > (c, d):  # 항상 작은 좌표가 먼저 오도록 정렬
            a, b, c, d = c, d, a, b
        blocked[a+c][b+d] = 1

    # 시작점 초기화
    dp[0][0] = 1

    # DP 계산
    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and blocked[2*i-1][2*j] == 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0 and blocked[2*i][2*j-1] == 0:
                dp[i][j] += dp[i][j - 1]

    # 결과 출력
    print(dp[n][m])