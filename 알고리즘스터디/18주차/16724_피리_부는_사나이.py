# https://www.acmicpc.net/problem/16724

'''
[문제]
    SAFE ZONE의 최소 개수 출력
    -> Blob 마다 Group을 지어서, Blob 내부에 Safearea를 하나씩 둔다
    -> Blob 갯수를 Count 한다
    MST와 유사하게 Blob을 생성해서 풀어보자

'''
import sys
def input(): return sys.stdin.readline().rstrip()



def dir_idx(c):
    if c == 'U':
        return 0
    elif c == 'L':
        return 1
    elif c == 'D':
        return 2
    elif c == 'R':
        return 3

def dfs(r, c):
    global group_cnt
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    i = dir_idx(grid[r][c])
    nr = r + dr[i]
    nc = c + dc[i]
    if not (0 <= nr < n and 0 <= nc < m):
        return 
        
    if group_grid[nr][nc] == -1:
        group_grid[nr][nc] = group_grid[r][c]
        dfs(nr, nc)
    elif group_grid[nr][nc] == group_grid[r][c]:
        return
    elif group_grid[nr][nc] != group_grid[r][c]:
        group_cnt -= 1
        
    
    


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    group_grid = [[-1] * m for _ in range(n)]
    group_cnt = 0
    group_id = 0
    

    
    for r in range(n):
        for c in range(m):
            if group_grid[r][c] == -1:
                group_id += 1
                group_cnt += 1
                group_grid[r][c] = group_id
                dfs(r,c)
    print(group_cnt)



