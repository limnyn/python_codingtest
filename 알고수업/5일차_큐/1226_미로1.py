def maze_bfs():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    grid = []
    start= [-1,-1]
    end = [-1,-1]
    for r in range(16):
        line = list(map(int, input()))
        
        for c in range(len(line)):
            if line[c] == 2:
                start = [r,c]
            elif line[c] == 3:
                end = [r,c]
        grid.append(line)

    dq = deque()
    dq.append(start)
    visited = [[False]*16 for _ in range(16)]
    visited[start[0]][start[1]] = True
    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i] 

            if 0 <= nr < 16 and 0 <= nc < 16:
                if grid[nr][nc] != 1 and visited[nr][nc] == False:
                    if grid[nr][nc] == 3:
                        return 1
                    elif grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        dq.append([nr,nc])

    return 0



from collections import deque
for _ in range(1, 11):
    t_c = int(input()) 
    print(f'#{t_c} {maze_bfs()}')