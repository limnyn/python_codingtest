# https://www.acmicpc.net/problem/1261
'''
[문제]
    0, 0에서 n,m까지 이동하기 위해 부숴야 할 최소 벽 갯수

[입력]
    1 <= N, M <= 100

[접근]
    0,0부터 시작해서 다익스트라 알고리즘을 통해 벽에 대해 비용이 1인 간선이라고 가정하고
    최단거리 계산을 통해 0,0부터 n,m까지의 최단거리를 계산하여 해당 값만큼 벽을 부수면 된다.
'''
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

def dijkstra(start):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    r,c = start
    distance = [[float('inf')] * m for _ in range(n)]
    distance[r][c] = 0
    
    hq = [(0, r, c)]

    while hq:
        dist, r, c = heapq.heappop(hq)    
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if distance[nr][nc] > dist +grid[nr][nc]:
                distance[nr][nc] = dist + grid[nr][nc]
                heapq.heappush(hq, (distance[nr][nc], nr, nc))
    
    return distance[-1][-1]
            

if __name__ == "__main__":
    m, n = map(int, input().split())
    
    grid = [list(map(int, list(input()))) for _ in range(n)]
    
    print(dijkstra((0,0)))