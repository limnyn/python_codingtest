# https://www.acmicpc.net/problem/4811

'''
w, h 에 대한 테이블 생성

1. dp[w][h] 값 존재 시 리턴
2. w가 0인 경우 1 리턴 
3. h가 0인 경우 반 조각이 존재하지 않는다
    따라서 [w - 1][h + 1] 값을 리턴한다.
4. h > 0 인 경우, 즉 반조각이 존재하는 경우 dp[w][h] = dp[w][h-1] + dp[w-1][h+1]

'''

dp = [[0] * 31 for _ in range(31)]

def init(w, h):
    if dp[w][h] > 0:  # dp 값이 존재한다면
        return dp[w][h]
    
    if w == 0:  # 한 조각이 아예 없는 경우
        return 1
    
    if h == 0:  # 반 조각이 없는 경우
        dp[w][h] = init(w - 1, h + 1)
    else:  # 반 조각도 있고, 한 조각도 있는 경우
        dp[w][h] = init(w, h - 1) + init(w - 1, h + 1)
    
    return dp[w][h]

init(30, 0)
while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][0])
