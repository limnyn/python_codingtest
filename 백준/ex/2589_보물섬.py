# https://www.acmicpc.net/problem/2589

"""
브루트포스 - BFS 
L인 모든 좌표에 대해 
BFS를 수행해서 최단 거리들을 찾고
해당 거리들 중 max값을 출력한다
 
파이썬 시간초과 pypy3 통과, 따라서 불필요한 실행 경우 제외
"""

from collections import deque
n, m = map(int,input().split())
grid = [input() for _ in range(n)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(start_r, start_c):

    # r, c에 대해서 BFS를 수행한다.
    dq = deque()
    dq.append((start_r, start_c))
    count = 0
    visited = [[0]*m for _ in range(n)]
    visited[start_r][start_c] = 1 # 방문한 곳
    
    

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and grid[nr][nc] == 'L':
                visited[nr][nc] = visited[x][y] + 1
                count = max(visited[nr][nc], count)
                dq.append((nr, nc))
    
    
    return count - 1



result = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 'L':
            # 시간을 더 줄이기 위해 양옆 또는 좌우에 끼어있는 L은 bfs를 하지 않는다
            if 0 <= r-1 and r+1 < n:
                if grid[r-1][c] == 'L' and grid[r+1][c] == 'L':
                    continue
            if 0 <= c-1 and c+1 < m:
                if grid[r][c-1] == 'L' and grid[r][c+1] == 'L':
                    continue
            result = max(result, bfs(r,c))

print(result)
        



# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW