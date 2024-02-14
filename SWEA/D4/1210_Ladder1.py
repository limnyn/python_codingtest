"""
사다리를 아래서 부터 위로 접근하면 결과가 나온다
"""

dr = [0, 0, -1]
dc = [-1, 1, 0]
for _ in range(10):
    t_c = int(input())
    grid = []
    
    for i in range(100):
        line = list(map(int, input().split()))
        if 2 in line:
            r, c = (i, line.index(2))
        grid.append(line)
    
    dir = 2
    while r > 0:
        
        if dir < 2:
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < 100 and 0 <= nc < 100:
                if grid[nr][nc] == 1:
                    r = nr
                    c = nc
                    continue
            
            dir = 2
            r = r + dr[2]
            c = c + dc[2]
            continue
        else:
            for i in range(3):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 100 and 0 <= nc < 100:
                    
                    if grid[nr][nc] == 1:
                        dir = i
                        r = nr
                        c = nc
                        break
            

            
         
    print(f'#{t_c} {c}')


    


    # print("#" + str(t_c + 1) + " " + str(count))
