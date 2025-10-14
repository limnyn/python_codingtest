# https://www.acmicpc.net/problem/1753

import sys, heapq
def input():return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    k = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))


    hq = []
    heapq.heappush(hq, (0, k))
    distance = [float("inf")] * (n + 1)
    distance[k] = 0

    while hq:
        dist, node = heapq.heappop(hq)

        for next, cost in graph[node]:
            if distance[next] > distance[node] + cost:
                distance[next] = distance[node] + cost
                heapq.heappush(hq, (distance[next], next))

    
    for i in range(1, n + 1):
        if distance[i] == float("inf"):
            print("INF")
        else:
            print(distance[i])
