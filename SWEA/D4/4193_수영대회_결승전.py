'''
bfs를 순회하면서 r, c, time을 넣어주면 될 거 같다
만약 4방향에 대해 [nr, nc]가 소용돌이 일 때
time % 3 == 0 이라면 deque에 [nr, nc, time + 3]을 넣는다

각 칸에 대해서 visited[nr][nc] > visited[r][c] + time이라면
visited[nr][nc] = visited[r][c] + time을 하면
해당 칸에 대해 가장 짧게 도착한 사긴을 알 수 있다.
'''

from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution():
    #입력
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))


    visited = [[1000]*n for _ in range(n)]
    visited[start[0]][start[1]] = 0
    # bfs 순회를 위해 처리
    dq = deque([])
    dq.append((start[0], start[1], 0))
    while dq:
        r, c, time = dq.popleft()
        time += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if end[0] == nr and end[1] == nc:
                    if visited[nr][nc] > time:
                        visited[nr][nc] = time
                    continue
                
                if grid[nr][nc] == 0:
                    if visited[nr][nc] > time:
                        visited[nr][nc] = time
                        dq.append((nr, nc, time))
                
                # 소용돌이는 시작시간부터 2초동안 못 지나가고 1초동안 지나갈 수 있다
                if grid[nr][nc] == 2:
                    next_time = time 
                    while(next_time % 3 != 0):
                        next_time += 1
                    if visited[nr][nc] > next_time:
                        visited[nr][nc] = next_time
                        dq.append((nr, nc, next_time))
    for v in visited:
        print(v)
    if visited[end[0]][end[1]] == 1000:
        return -1
    return visited[end[0]][end[1]]


for t_c in range(1, int(input()) + 1):
    print(f"#{t_c} {solution()}")
# time % 3 == 0 이라면 deque에 [nr, nc, time + 3]을 넣는다

# 각 칸에 대해서 visited[nr][nc] > visited[r][c] + time이라면
# visited[nr][nc] = visited[r][c] + time을 하면
                
                    


# 4
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 0 0
# 1 1