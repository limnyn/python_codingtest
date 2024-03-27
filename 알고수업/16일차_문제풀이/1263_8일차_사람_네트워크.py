INF = float('INF')
grid = []
n = 0
def floyd_washall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if grid[i][j] > grid[i][k] + grid[k][j]:
                    grid[i][j] = grid[i][k] + grid[k][j]                    
                    
def solution():
    global grid, n
    line = list(map(int, input().split()))
    n = line[0]
    grid = []
    for i in range(n):
        row = line[n*i+1:n*(i+1)+1]
        for j in range(n):
            if row[j] == 0:
                row[j] = INF
        grid.append(row)    

    floyd_washall()
    result = INF
    for i, g in enumerate(grid):
        result = min(sum(g) - g[i], result)
    return result

for t_c in range(1, int(input())+1):
    print(f"#{t_c} {solution()}")


