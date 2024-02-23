"""
- dfs로 탐색

in dfs
    result = max(length, result)
    for 4방향:
        다음 칸이 범위내에 있고 방문한 적이 없으면
            만약 다음칸이 클때
                if is_digged = False: 아직 안팠으면
                    여기서 k만큼 팠을 때 현재 grid[r][c]보다 작으면
                    isVisited[nr][nc] = True
                    dfs(nr, nc, length + 1, is_digged=True)
            안막혔을 때
                    isVisited[nr][nc] = True
                    dfs(nr,nc, length + 1, is_digged=is_digged)
    isVisited[r][c] = False
             
"""

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def dfs(r, c, cnt, is_digged):
    global result
    global visited
    global grid

    result = max(cnt, result)
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < n:
            if visited[nr][nc] == False:
                if grid[nr][nc] >= grid[r][c]:
                    if is_digged == False and grid[nr][nc] - k  < grid[r][c]:
                        tmp = grid[nr][nc]
                        grid[nr][nc] = grid[r][c] - 1
                        dfs(nr, nc, cnt + 1, True)
                        grid[nr][nc] = tmp
                        
                else:
                    dfs(nr,nc, cnt + 1, is_digged)
    visited[r][c] = False

    





                
for t_c in range(1, int(input())+1):
    n, k = map(int, input().split())
    start = 0
    satrts = [] # 제일 높은 등산로의 좌표들
    result = -1e9
    grid = []
    for r in range(n):
        line = list(map(int, input().split()))
        if max(line) > start:
            start = max(line)
        grid.append(line)
    starts = []
    for r in range(n):
        for c in range(n):
            if grid[r][c] == start:
                starts.append([r,c])

    for start_r, start_c in starts:
        visited = [[False]*n for _ in range(n)]
        dfs(start_r,start_c,1,False)
        # print(start_r, start_c)
    print(f"#{t_c} {result}")
