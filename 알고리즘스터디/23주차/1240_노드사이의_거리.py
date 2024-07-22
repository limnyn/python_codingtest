# https://www.acmicpc.net/problem/1240
'''
m번 bfs를 탐색하자
'''
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


def bfs(start, end):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    visited = [-1] * n
    visited[start] = 0
    dq = deque([])
    dq.append((start, 0))

    while dq:
        node, dist = dq.popleft()
        for next_dist, next in graph[node]:
            if visited[next] == -1:
                visited[next] = dist + next_dist
                dq.append((next, visited[next]))
            if next == end:
                return visited[end]

    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        start, end, dist = map(int, input().split())
        graph[start - 1].append((dist, end - 1))
        graph[end - 1].append((dist, start - 1))
    
    for _ in range(m):
        start, end = map(int, input().split())
        print(bfs(start - 1, end - 1))


        