# https://www.acmicpc.net/problem/2667

n = int(input())
grid = []
for r in range(n):
    line = []
    for num in input():
        if num == "0":
            line.append(0)
        else:
            line.append(1)
    grid.append(line)


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

from collections import deque


def bfs(r, c):
    if grid[r][c] == 1:
        count = 1
        dq = deque()
        dq.append([r, c])
        grid[r][c] = -1
        while dq:
            r, c = dq.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    count += 1
                    grid[nr][nc] = -1
                    dq.append([nr, nc])
        return count
    else:
        return 0


answer = []
for r in range(n):
    for c in range(n):
        rc_sum = bfs(r, c)
        if rc_sum:
            answer.append(rc_sum)

print(len(answer))
for ans in sorted(answer):
    print(ans)
