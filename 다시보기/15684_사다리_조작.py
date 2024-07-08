# https://www.acmicpc.net/problem/15684
'''
[문제]
현재 사다리 상황이 주어졌을 때 
모든 시작점에 대해 
i번째 출발해서 i번째로 나오게 하기 위해서
추가로 놓아야하는 사다리의 최소 갯수 구하기

[입력]
    세로 선의 개수 2 <= N <= 10
    가로 선의 개수 0 <= M <= (N-1) * H
    가로 선을 놓을 수 있는 위치의 개수 1 <= H <= 30

[접근]
    백트래킹 
'''
import sys
def input(): return sys.stdin.readline().rstrip()

def is_exit_success():
    '''
    시작점에서 끝점으로 나오는지 확인
    만약 가능하면 True else False
    '''
    for start_col in range(n):
        col = start_col
        row = 0
        while row < h:
            if grid[row][col] == 1:
                col += 1
            elif col > 0 and grid[row][col-1] == 1:
                col -= 1
            row += 1
        if col != start_col:
            return False
    return True

def dfs(ladder, start):
    global result
    if ladder >= result:
        return
    if is_exit_success():
        result = ladder
        return
    if ladder == 3:
        return

    for i in range(start, len(positions)):
        row, col = positions[i]
        if is_set_possible(col, row):
            grid[row][col] = 1
            dfs(ladder + 1, i + 1)
            grid[row][col] = 0

def is_set_possible(col, row):
    '''
    해당 위치에 놓을 수 있는지 확인
    놓을 수 있으면 True 반환 else False
    '''
    if grid[row][col] == 1:
        return False
    if col > 0 and grid[row][col-1] == 1:
        return False
    if col < n - 1 and grid[row][col + 1] == 1:
        return False
    return True

if __name__ == "__main__":
    n, m, h = map(int, input().split())
    grid = [[0] * n for _ in range(h)]
    result = 4 # 만약 결과가 4가 나온다면 -1 출력
    positions = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        grid[a-1][b-1] = 1

    for i in range(h):
        for j in range(n-1):
            if grid[i][j] == 0 and grid[i][j+1] == 0:
                positions.append((i, j))

    dfs(0, 0)
    if result >= 4: 
        print(-1)
    else: 
        print(result)
