# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

for t_c in range(1, int(input())+1):
    n, m = map(int, input().split())
    
    grid = [[0]*n for _ in range(n)]
    grid[n//2-1][n//2-1:n//2+1] = [2, 1]
    grid[n//2][n//2-1:n//2+1] = [1, 2]
    # print(grid)
    
    def turn(r, c, num):
        # 각 방향에 대해 
        # 다른 숫자가 나오면 무시
        # 같은 숫자가 나온다면 그 사이에 있는 수 전체 변환
        grid[r][c] = num
        dir = [[-1,0],[-1, 1],[0, 1],[1, 1],[1, 0],[1,-1],[0,-1],[-1,-1]]
        for i in range(8):
            dr,dc = dir[i]
            nr = r + dr
            nc = c + dc
            
            while(1):
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] != num:
                        if grid[nr][nc] != 0:
                            nr += dr
                            nc += dc
                        else:
                            break
                    elif grid[nr][nc] == num:
                        length = max(abs(nr-r), abs(nc-c))
                        for k in range(1, length):
                            grid[r + dr*k][c + dc*k]=num
                        break
                else:
                    break                        
                
    for _ in range(m):
        r, c, num = map(int, input().split())
        turn(r-1,c-1,num)
        
    black_cnt = 0
    white_cnt = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                black_cnt += 1
            elif grid[r][c] == 2:
                white_cnt += 1
    print(f'#{t_c} {black_cnt} {white_cnt}')