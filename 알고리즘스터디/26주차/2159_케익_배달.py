# https://www.acmicpc.net/problem/2159
'''
[문제]
순서대로 목적지 또는 목적지 주변에 케익을 나둘 때 최단 거리로 문제를 수행하기

[입력]
1 ≤ N, X, Y ≤ 100,000

[접근 - DP]
i번째 목적지 및 주변 5개의 좌표에 대해
5개의 좌표까지의 최단거리를 리스트로 들고 있다고 가정할 때
d[i][0] = min(d[i-1][0~4] + 거리) 
'''
from collections import deque
import sys, copy
def input(): return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    start_coord = list(map(int, input().split()))
    coords = deque([])
    for _ in range(n):
        coords.append(list(map(int, input().split())))
    
    dr = [0, -1, 0, 1, 0]
    dc = [0, 0, -1, 0, 1]
    before_min_dist = []
    
    # 0~1번째 목적지에 놓을수 있는 좌표와 그때의 거리를 저장
    sr, sc = start_coord
    r, c = coords.popleft()
    for i in range(5):
        nr = r + dr[i]
        nc = c + dc[i]
        dist = abs(nr - sr) + abs(nc - sc)
        before_min_dist.append((nr, nc, dist))
        
    # 1~n번째 로직에 대해 수행
    while coords:
        '''
        i번째 목적지의 5개의 각 좌표에 대해
            i-1번째 목적지의 5개의 좌표 + 거리의 최솟값을 저장한다.
        '''
        r, c = coords.popleft() # i번째 목적지
        
        next_min_dist = [(-1, -1, float('inf')) for _ in range(5)]
        
        for i in range(5):
            nr = r + dr[i]
            nc = c + dc[i]
            
            for before_r, before_c, dist in before_min_dist:
                n_dist = abs(nr - before_r) + abs(nc - before_c)
                if next_min_dist[i][2] > n_dist + dist:
                    next_min_dist[i] = (nr, nc, n_dist + dist)
                
        
            
        before_min_dist = copy.deepcopy(next_min_dist)

    result = float('inf')
    for r, c, dist in before_min_dist:
        result = min(result, dist)
        
    print(result)