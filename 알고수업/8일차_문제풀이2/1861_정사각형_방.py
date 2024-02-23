

from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(r, c):
    dq = deque([])
    max_result = 0
    cnt = 0
    dq.append([r,c, cnt])
    
    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True

    while dq:
        r, c, cnt = dq.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == False:
                    if grid[nr][nc] == grid[r][c] + 1:
                        visited[nr][nc] = True
                        max_result = max(max_result, cnt+1)
                        dq.append([nr,nc, cnt+1])
    return max_result
    
for t_c in range(1, int(input())+1):
    n = int(input())
    max_length = -1
    result = [0,0]
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    for r in range(n):
        for c in range(n):
            #좌우 또는 상하에 낀 좌표인 경우는 bfs로 count 하지 않는다. 어차피 최대가 될 수 없다.
            if 0 < r < n-1:
                if (grid[r-1][c] == grid[r][c] - 1 and grid[r+1][c] == grid[r][c] + 1) or (grid[r-1][c] == grid[r][c] + 1 and grid[r+1][c] == grid[r][c] - 1): 
                    continue
            if 0 < c < n-1:
                if (grid[r][c-1] == grid[r][c] - 1 and grid[r][c+1] == grid[r][c] + 1) or (grid[r][c-1] == grid[r][c] + 1 and grid[r][c+1] == grid[r][c] - 1): 
                    continue
            length = bfs(r, c)
            if length > max_length:
                max_length = length
                result[0] = grid[r][c]
                result[1] = length
            if length == max_length:
                if result[0] > grid[r][c]:
                    result[0] = grid[r][c]
                

    print(f"#{t_c} {result[0]} {result[1]+1}")
            
