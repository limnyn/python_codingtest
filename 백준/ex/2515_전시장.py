# https://www.acmicpc.net/problem/2515
"""
[문제]
그림마다 비용이 정해져 있을 때
그림을 1열로 세워서 가려지지 않은 부분이 S 이상인 경우에 그림을 판매한다.
가장 많이 판매하도록 그림을 세우는 경우

[접근]
DP 사용

dp[i] = max(
            (i-1번째 그림까지 가능한 경우에서의 최대 값),
            (
                i번쨰 그림의 비용 
                + (i번째 그림 높이 - s)번 그림까지의 최대값 + 현재 그림 비용
            )   
        )

여기서 j번 인덱스
        = (i번째 그림 높이 - s)번 그림 위치
        를 구하기 위해서 이분탐색을 통해 구한다

"""
import sys, bisect
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, s = map(int, input().split())
    
    paintings = []

    for _ in range(n):
        h, c = map(int, input().split())
        paintings.append((h,c))

    paintings.sort()
    heights = [h for h, _ in paintings]

    dp = [0] * (n)
    dp[0] = paintings[0][1]

    for i in range(1, n):
        h, c = paintings[i]

        j = bisect.bisect_left(heights, h - s + 1)

        dp[i] = max(dp[i-1], dp[j - 1] + c)
    print(dp[-1])
