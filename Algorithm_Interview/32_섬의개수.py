# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.

# 5
# 4
# 11000
# 11000
# 00100
# 00011
n = int(input())
m = int(input())
grid = []
for _ in range(m):
    grid.append(list(map(int, input())))


def dps(x, y):
    if (x <= -1 or x >= n or y <= -1 or y >= m):
        return False
    if(grid[y][x] == 1):
        grid[y][x] = 0
        dps(x+1, y)
        dps(x, y+1)
        dps(x-1, y)
        dps(x, y-1)
        return True
    return False

count = 0
for i in range(m):
    for j in range(n):
        if dps(j,i) == True:
            count+=1
print(count)