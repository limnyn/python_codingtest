# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

for t_c in range(1, int(input())+1):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
        
    n = int(input())
    orders = list(input())   

    
        
    def move(order, r, c):
        
        dir = [[-1,0,'^'],[1,0,'v'],[0,-1,'<'],[0,1,'>']]
        if order == 'U':
            num = 0
        elif order == 'D':
            num = 1
        elif order == 'L':
            num = 2
        elif order == 'R':
            num = 3
        elif order == 'S':
            num = 4
        if num < 4:
            x,y,z = dir[num]
            if 0<=r+x<h and 0<=c+y<w and grid[r+x][c+y] not in  ['-','*','#']:
                grid[r][c] = '.'
                grid[r+x][c+y] = z
                r, c = r+x, c+y
            else:
                grid[r][c] = z
            return r, c

        for i in range(4):
            if grid[r][c] == dir[i][2]:
                num = i
                break

        x, y, z = dir[num]
        nr, nc = r+x, c+y
        while(1):
            if 0<=nr<h and 0<=nc<w:
                if grid[nr][nc] == '*':
                    grid[nr][nc] = '.'
                    break
                elif grid[nr][nc] == '#':
                    break
                nr += x
                nc += y
            else:
                break
        return r, c
    
    for r in range(h):
        for c in range(w):
            if grid[r][c] in ['^','v','<','>']:
                nr, nc = r, c
                
                
    for order in orders:
        nr, nc = move(order, nr, nc)
    ''.join(grid[0])
    result = [''.join(x) for x in grid]
    
    print(f'#{t_c} ',end='')
    for r in result:
        print(r)
    
'''

.   평지
*   벽돌벽
#   강철벽
-   물(전차는 들어갈 수 없다)
^   위쪽을 바라보는 전차(아래는 평지이다.)
v  아래쪽을 바라보는 전차(아래는 평지이다.)     
<   왼쪽을 바라보는 전차(아래는 평지이다.)
>   오른쪽을 바라보는 전차(아래는 평지이다.)


명령
U   전차가 바라보는 방향을 위로 바꾸고, 한칸 위의 칸이 평지라면 그 칸으로 이동
D   전차가 바라보는 방향을 아래로 바꾸고, 한칸 아래의 칸이 평지라면 그 칸으로 이동
L   전차가 바라보는 방향을 왼쪽으로 바꾸고, 한칸 왼쪽의 칸이 평지라면 그 칸으로 이동
R   전차가 바라보는 방향을 오른쪽으로 바꾸고, 한칸 오른쪽의 칸이 평지라면 그 칸으로 이동
S   전차가 현재 바라보고 있는 방향으로 포탄 발사

만약 이동하려 할 때 맵밖이라면 이동하지 않고 무시. 방향만 전환
포탄은 방향을 따라 벽/맵밖으로 갈 때까지 직진
강철벽에 맞으면 아무 일도 일어나지 않고 벽돌벽은 맞으면 평지가 된다. 맵밖으로 나가면 아무일 x
초기 게임 맵의 상태와 사용자가 넣을 입력이 순서대로 주어질 때, 모든 입력을 처리하고 나면 게임 맵의 상태가 어떻게 되는 지 구하라.


'''