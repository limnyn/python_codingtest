def isomok(grid, n, r, c):

    if 0 <= c - 2 and c + 2 < n:
        if sum(grid[r][c-2:c+2+1]) == 5:
            return True
    if 0 <= r - 2 and r + 2 < n:
        tmp = [grid[i][c] for i in range(r-2,r+2+1)]
        if sum(tmp) == 5:
            return True
        
    if 0 <= r - 2 and r + 2 < n and 0 <= c - 2 and c + 2 < n:
        cnt1, cnt2 = 0, 0
        for i in range(5):
            if grid[r - 2 + i][c - 2 + i] == 1:
                cnt1 += 1
            if grid[r - 2 + i][c + 2 - i] == 1:
                cnt2 += 1
        if cnt1 == 5 or cnt2 == 5:
            return True
    return False
    
        

    
for t_c in range(1, int(input())+1):
    n = int(input())
    grid = []
    for _ in range(n):
        line = []
        for c in list(input()):
            if c == '.':
                line.append(0)
            elif c == 'o':
                line.append(1)
        grid.append(line)
    result = "NO"
    for r in range(n):
        for c in range(n):
            if isomok(grid, n,r,c):
                result = "YES"
                
    print(f'#{t_c} {result}')
    


