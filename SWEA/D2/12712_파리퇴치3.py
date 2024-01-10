 
def kill_fly(r, c, grid, n, m):
    
#+
    fly_count_1 = grid[r][c]
    for i in range(1,m):    
        # -i 0
        if 0 <= r - i:
            fly_count_1 += grid[r-i][c]
        # 0 -i
        if 0 <= c - i:
            fly_count_1 += grid[r][c-i]
        # +i 0
        if r + i < n:
            fly_count_1 += grid[r+i][c]
        # 0 +i
        if c + i < n:
            fly_count_1 += grid[r][c+i]
#x
    fly_count_2 = grid[r][c]
    for i in range(1,m):    
        # -i -i
        if 0 <= r - i and 0<= c - i:
            fly_count_2 += grid[r-i][c-i]
        # -i +i
        if 0 <= r - i and c + i < n:
            fly_count_2 += grid[r-i][c+i]
        # +i -i
        if r + i < n and 0<= c - i:
            fly_count_2 += grid[r+i][c-i]
        # +i +i
        if r + i < n and c + i < n:
            fly_count_2 += grid[r+i][c+i]

    return max(fly_count_1, fly_count_2)
                    




for t_c in range(1, int(input())+1):
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]
    result = -1
    
    for i in range(n):
        for j in range(n):
            kill_count = kill_fly(i, j,grid,n,m)
            result = kill_count if kill_count > result else result

    print(f"#{t_c} {result}")
