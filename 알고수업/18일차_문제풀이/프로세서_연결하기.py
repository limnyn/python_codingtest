'''
    목표 
        -> '최대한 많은 core에 전원을 연결하였을 경우', 전선 길이의 합을 구하기
    
    문제 조건
        7 <= N <= 12
        Core의 개수는 최소 1개 이상 12개 이하
        최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.

    
    접근 방법
        1. Core를 뽑는 멱집합
            
            N과 Core의 개수가 적고, '최대한 많은 core에 전원 연결' 조건에 따라서
            "백트래킹"을 이용할 수 있을 거 같다

            N의 최대값 12
            
            각 코어에 대해 방향을 5개(4방향 + 연결 안하는 경우)를 선택한다면
                5^12 경우
                이 중 백트래킹을 통해 겹치는 경우 탐색을 하지 않는다면 줄일 수 있을 것 같다.
            
        2. 조합에 대해 전선의 길이를 구하는 경우
            각 조합의 방향에 따라 방문처리하며 전진을 한다.
            만약 전진 방향이 방문되어 있으면 return -1
            그 외에는 전체 전선 길이를 반환한다.
    
'''
dr = [-1, 0, 1, 0, 0]
dc = [0, 1, 0, -1, 0]

def calc(combi):
    visited = [[0]*N for _ in range(N)]
    wire_len = 0
    core_cnt = 0
    for idx in range(CORE_LEN):
    
        spot_r, spot_c = core_spot[idx]
        visited[spot_r][spot_c] = 1

    for idx in range(CORE_LEN):
        nr, nc = core_spot[idx]
        dir = combi[idx]
        if dir == 4:
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                core_cnt += 1
            continue
        if dir < 4:
            core_cnt += 1

        # if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
            
            nr = nr + dr[dir]
            nc = nc + dc[dir]
            while 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 1:
                    return -1, -1
                
                visited[nr][nc] = 1
                wire_len += 1
                nr = nr + dr[dir]
                nc = nc + dc[dir]

    return core_cnt, wire_len
        


    

def backtracking(combi):
    global max_core_cnt, min_wire_len

    if len(combi) == CORE_LEN:
        # print(combi)
        core_cnt, wire_len = calc(combi)
        if core_cnt != -1:
            if max_core_cnt == 0:
                max_core_cnt = core_cnt

            if core_cnt == max_core_cnt:
                # max_core_cnt = core_cnt
                min_wire_len = min(wire_len, min_wire_len)
            else:
                return False
        



    else:
        for dir in range(5):
            backtracking(combi + [dir])
        


if __name__ == "__main__":
    for t_c in range(1, int(input())+1):
        grid = []
        max_core_cnt = 0
        min_wire_len = 1e9

        N = int(input())    
        core_spot = []
        for r in range(N):
            line = list(map(int, input().split()))
            for c in range(N):
                if line[c] == 1:
                    core_spot.append((r,c))
            grid.append(line)
        CORE_LEN = len(core_spot)
        backtracking([])
        print(f"#{t_c} {min_wire_len}")

            
    




'''
1
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''