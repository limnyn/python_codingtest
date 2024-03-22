'''
bfs를 돌면서 visited한 노드에 대해
해당 노드보다 짧은 시간에 visted 할 수 있다면
즉, visisted[nr][nc] > visited[r][c] + grid[r][c]라고 할 때
visited[nr][nc] = visited[r][c] + grid[r][c]
dq.append((nr, nc))를 한다
'''

from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution():
    dq = deque([])
    n = int(input())
    grid = [list(map(int,list(input()))) for _ in range(n)]

    visited = [[1e9]*n for _ in range(n)]


    dq.append((0,0))
    visited[0][0] = grid[0][0]

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] > visited[r][c] + grid[r][c]:
                    visited[nr][nc] = visited[r][c] + grid[r][c]
                    dq.append((nr, nc))
    return visited[n-1][n-1]

for t_c in range(1, int(input())+ 1):
    print(f"#{t_c} {solution()}")

