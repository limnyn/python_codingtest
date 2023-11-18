spots = {}
grid = [[0] * 300 for _ in range(300)]
level = 0
for i in range(1, 300):
    for j in range(i,0,-1):
        level += 1
        # print(i-j+1,j, level)
        grid[i-j+1][j] = level
        spots[level] = (i-j+1, j)
        
for t_c in range(1, int(input())+1):
        

    p, q = map(int, input().split())

    l = spots[p]
    r = spots[q]
    print(f'#{t_c} {grid[l[0]+r[0]][l[1]+r[1]]}')

        
        
        
        