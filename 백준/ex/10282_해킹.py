# https://www.acmicpc.net/problem/10282
'''
특정지점에서 다른 연결된 모든 지점까지의 최단시간(거리)
+ 자신과 연결된 노드의 갯수 구하기

-> 다익스트라를 통해 구하기
'''

import sys, heapq
def input(): return sys.stdin.readline().rstrip()

def dijkstra(start):
    visited = [float('inf')] * n
    visited[start] = 0

    hq = []

    heapq.heappush(hq, (0, start))

    while hq:
        dist, node = heapq.heappop(hq)

        if visited[node] < dist:
            continue

        for next, cost in graph[node]:
            if visited[next] > dist + cost:
                visited[next] = dist + cost
                heapq.heappush(hq, (visited[next], next))
    
    result = [x for x in visited if x != float('inf')]
    print(len(result), max(result))

if __name__ == "__main__":

    for _ in range(int(input())):
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n)]
        
        for _ in range(d):
            a, b, s = map(int, input().split())
            a, b = a - 1 , b - 1
            graph[b].append((a, s)) # b가 감염되면 s초 후 a도 감염된다.

        dijkstra(c - 1)
