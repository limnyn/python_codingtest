import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if grid[r][c] < grid[nr][nc]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc) +1)
        
    return dp[r][c]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]





for r in range(n):
    for c in range(n):
        dfs(r,c) 

print(max(map(max, dp))+1)
