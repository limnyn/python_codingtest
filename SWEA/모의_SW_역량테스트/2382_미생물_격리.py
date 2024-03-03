
"""
K개의 미생물 군집
N*N 정사각형 셀
n <= 100, 격리시간 M <= 1000
k = 군집의 갯수

구현

    - "시간"에 따라 군집들에 대해 "이동"한다.
    - "이동" 이 완료되면 각 칸에 대해 처리를 해 준다.


    def 이동(군집)
        ->> 현재 grid에는 한 칸에 한 값만 있는 상태
        다음 칸에 대해 군집을 삽입한다
        grid[nr][nc].append([micro, dir])
        grid[r][c] = []
        
    
    def 처리
        ->> 현재 grid에는 한 칸에 두개 이상 존재할 수 있다.

        
        next_grid = copy.deepcopy(grid)
        if (r,c) == 약품구역:
            방향을 반전, micro = int(micro/2)
            if micro != 0:
                next_grid[r][c] = (micro, 반전된 방향)
        elif (r,c)에 여러 셀이 존재할 때:
            -> elif len(grid[r][c]) > 1:

            sort를 통해 최대값으로 방향을 정하고 
            sum으로 미생물 합 계산
            next_grid[r][c] = [micro_sum, 결과 방향]
        else:
            처리할 필요 없음
            next_grid[r][c] = [micro, 방향]

        grid = copy.deepcopy(next_grid)

    Main 함수
    -> M 시간 동안 이동 - 처리 반복
    for _ in range(m):
        move()
        calc()


    result = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                result += grid[r][c][0]

"""


#1시간 후 이동 방향으로 다 옮겨주기
def move():
    global grid
    new_grid = [[[] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                micro, dir = grid[r][c]
                nr = r + dr[dir]
                nc = c + dc[dir]
                new_grid[nr][nc].append([micro, dir])
    grid = new_grid


#약품구역인지 확인
def is_drug_spot(r, c):
    if r == 0 or c == 0 or r == n-1 or c == n-1:
        return True
    else:
        return False

#약품구역일 때 방향 뒤집어주기
def dir_reverse(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    elif dir == 3:
        return 2

#이동이 완료된 각 칸에 대한 처리함수
def calc():
    global grid
    next_grid = [[[] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                # 하나인 경우
                if len(grid[r][c]) == 1:
                    micro, dir = grid[r][c][0]
                    if is_drug_spot(r, c):
                        micro = int(micro/2)
                        dir = dir_reverse(dir)
                    next_grid[r][c] = [micro, dir]
                # 두개 이상인 경우
                else:
                    micro_sum = 0
                    micro_max = -1e9
                    next_dir = -1
                    for micro, dir in grid[r][c]:
                        micro_sum += micro
                        if micro > micro_max:
                            micro_max = micro
                            next_dir = dir
                    next_grid[r][c] = [micro_sum, next_dir]
    
    grid = next_grid

                        

                

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for t_c in range(1, int(input())+1):

    n, m, k = map(int, input().split())
    grid = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        r, c, micro, dir  = list(map(int, input().split()))
        grid[r][c] = [micro, dir-1]
    

    for _ in range(m):
        move()
        calc()
    result = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                result += grid[r][c][0]
    print(f"#{t_c} {result}")
   
