# https://www.acmicpc.net/problem/16234


# dfs로 다 순회할 때 x,y좌표들을 리스트에 넣고 왔다감 표시를 blobs에 한다.
# 순회가 끝나면 setlist에 좌표모음을 넣는다
# 모든 좌표에 대해 수행한다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, left, right = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

 

dx = [1, 0, -1 ,0]
dy = [0, -1, 0 ,1]


def dfs(sets:list ,r,c):
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if blobs[x][y] != 0:
            continue
        
        dif = abs(grid[r][c] - grid[x][y])
        if dif <= right and dif >= left:
            blobs[x][y] = -1
            sets.append((x,y,grid[x][y]))
            dfs(sets, x, y)



day = 0
while(1):
    setlist = []
    blobs = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if blobs[r][c] == -1:
                continue
            is_in = False
            for sets in setlist:
                if (r,c,grid[r][c]) in sets:
                    is_in = True
            if is_in == True:
                continue
            s = [(r,c,grid[r][c])]
            blobs[r][c] = -1
            dfs(s, r, c)
   
            # s = set(s)
            setlist.append(s)
    # print(setlist)
    if len(setlist) == n*n:
        break
    
    for aset in setlist:
        setavg = 0
        for x, y, a in aset:
            setavg += a
        setavg //= len(aset)
        for x, y, a in aset:
            grid[x][y] = setavg
            
    day += 1
    
        
print(day)
