'''
n 의 최대값 20

bfs 수행 시
    20*20 칸에 대해 20*20번 탐색 
    -> 160,000번 연산

좌표별 bfs를 탐색하면서 최대값을 출력해보자
'''
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

max_house = 0
n = 0
m = 0
grid = []


def bfs(start_r,start_c):
    global max_house, n, m, grid
    k = 1
    profit = 0
    sales = grid[start_r][start_c]

    dq = deque([])
    next_dq = deque([])
    visited = [[False] * n for _ in range(n)]
    dq.append((start_r, start_c))
    visited[start_r][start_c] = True

    cost = k * k + (k-1) * (k-1)
    profit = sales*m -cost
    if profit >= 0:
        max_house = max(sales, max_house) 


    
    
    while dq: #여기서 언제까지 순회할 지 정해야 한다.
        while dq:
            r, c = dq.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < n:
                    if visited[nr][nc] == False:
                        if grid[nr][nc] == 1:
                            sales += 1
                        visited[nr][nc] = True
                        next_dq.append((nr,nc))

        k += 1
        cost = k * k + (k-1) * (k-1)
        profit = sales*m -cost
        if profit >= 0:
            max_house = max(sales, max_house) 
        
        dq = next_dq
        next_dq = deque([])


        

def solution():
    global n, m, grid, max_house
    max_house = 0
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    for r in range(n):
        for c in range(n):
            bfs(r,c)
    return max_house


if __name__ == '__main__':
    for t_c in range(1, int(input())+1):
        print(f"#{t_c} {solution()}")