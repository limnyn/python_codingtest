# https://www.acmicpc.net/problem/1697


import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001


def bfs(n):
    dq = deque()
    dq.append(n)

    while dq:
        node = dq.popleft()
        if node == k:
            print(visited[node])
            break
        for next in (node + 1, node - 1, node * 2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[node] + 1
                dq.append(next)


bfs(n)
