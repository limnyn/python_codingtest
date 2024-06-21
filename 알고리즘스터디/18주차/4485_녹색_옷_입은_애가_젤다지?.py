# https://www.acmicpc.net/problem/4485
'''
[문제]
    (0,0)에서 (n-1,n-1)까지 최소 비용으로 도달하기

[입력]
    2 <= N <= 125

[접근]
    (0,0)에서 (n-1,n-1)까지 최소 비용으로 도달하기
    -> 다익스트라를 사용해서 하나의 출발점에서 모든 노드에 대한 최단거리를 계산할 수 있다
'''
import sys, heapq
def input(): return sys.stdin.readline()


def dijkstra(n):
    grid = [list(map(int, input().split())) for _ in range(n)]   
    dist = [[float('inf')]* n for _ in range(n)]
    dist[0][0] = grid[0][0]

    pq = []
    heapq.heappush(pq, (dist[0][0], 0, 0))

    while pq:
        current_cost, r, c = heapq.heappop(pq)

        if r == n-1 and c == n-1:
            return current_cost
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                new_cost = current_cost + grid[nr][nc]
                if dist[nr][nc] > new_cost:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return dist[n-1][n-1] 


if __name__ == "__main__":
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    
    idx = 1
    n = int(input())
    while n != 0:
        print(f"Problem {idx}: {dijkstra(n)}")
        n = int(input())
        idx += 1
    


    