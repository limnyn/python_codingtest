# https://www.acmicpc.net/problem/1987
"""
"""
import sys
def input(): return sys.stdin.readline().rstrip()

trace = [False] * 26
grid = []
result, R, C = 0, 0, 0
def get_idx(char):
    return ord(char) - ord('A')


def dfs(r, c, length):
    global result, R, C

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    #최대 경로 반환
    result = max(result, length)
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            idx = get_idx(grid[nr][nc])
            if trace[idx] == 0:
                trace[idx] = 1
                dfs(nr, nc, length + 1)
                trace[idx] = 0
            
def main():
    global result, R, C, grid
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    
    trace[get_idx(grid[0][0])] = True
    dfs(0, 0, 1)
    print(result)
    

if __name__ == "__main__":
    main()