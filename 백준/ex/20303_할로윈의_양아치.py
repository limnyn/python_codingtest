# https://www.acmicpc.net/problem/20303
'''
[목표]
K 미만의 아이들을 선택해 가장 많은 사탕 구하기
-> Knapsack 문제 (아이들 수 : 무게, 사탕 : 가치)

여기서 아이들의 친구 관계를 통해 친구 집단을 하나의 아이로 묶는 과정을 통해
그룹별로 사탕 수와 아이수를 map 해서 그룹별 (아이들 수 : 가치)를 구하자

그룹별 나누기
-> visited 1차원 방문 배열 만들고 각 시작점별로 BFS 돌아서 연결된 노드 수 : 가치 쌍으로 등록하기
'''
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


def friend_group(start):

    cnt = 0
    candy = 0
    dq = deque([start])

    while dq:
        node = dq.popleft()
        cnt += 1
        candy += children[node]

        for next in graph[node]:
            if visited[next] == False:
                visited[next] = True
                dq.append(next)

    group_candy.append((cnt, candy))
    return
    


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    children = list(map(int, input().split()))
    
    visited = [False] * n
    graph = [[] for _ in range(n)]

    group_candy = [(0,0)]
    for _ in range(m):
        src, dst = map(int, input().split())
        src -= 1 
        dst -= 1
        graph[src].append(dst)
        graph[dst].append(src)
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            friend_group(i)

    #Knapsack style DP 연산 시작
    row, col = len(group_candy) - 1, k - 1 # k 미만의 아이들 중 최대 값
    dp = [[0] * (col + 1) for _ in range(row + 1)]

    for r in range(1, row + 1):
        for c in range(1, col + 1):
            if c >= group_candy[r][0]:
                dp[r][c] = max(dp[r - 1][c - group_candy[r][0]] + group_candy[r][1], dp[r-1][c])
            else:
                dp[r][c] = dp[r-1][c]
    
    print(dp[-1][-1])


