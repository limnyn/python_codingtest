'''
활주로 건설

NxN 그리드에 대해
각 행|열 마다 활주로가 가능한지 검사하는 문제

6 <= N <= 20

지형의 높이 
    1 ~ 6
경사로 길이 X 
    2 <= X <= 4


활주로 조건 
    1. 활주로가 끝날 때 까지 높이가 유지되어야 한다.
    2. 이미 방문한 활주로에 대해서는 활주로 생성 불가
    3. 활주로가 좌표를 벗어나는 경우 생성 불가

testcase
    3 3 3 2 1 1
    
    for i in range(1, n-활주로 길이):
        만약 이전 좌표와 차이가 난다면
            활주로 설치 판별 가능하면
                활주로 설치

def 활주로 설치 판별
    1. 현재 좌표가 이미 방문한(활주로가 설치된)자리인지 확인
    2. 현재 값에 대해서 활주로 길이만큼 높이가 같은지 확인해 본다.
    3. 좌표를 벗어나는지 확인 



'''


'''
i는 1부터 탐색
만약 이전과 높이가 다르다면?
    
    1. 이전 좌표보다 높다면
        이전 좌표들에 대해 활주로를 건설해야함
    2. 이전 좌표보다 낮다면
        이후 좌표들에 대해 활주로를 건설해야함
    
이전 좌표들에 대해 활주로 건설
    
    이전 좌표부터 x만큼 진행하면서
        if 높이가 이전좌표와 같고 방문한 적이 없으면
            방문처리하고
        else:
            건설 불가 처리

이후 좌표들에 대해 활주로 건설
    
    현재 좌표부터 x만큼 진행하면서
        if 높이가 현재 좌표와 같고 방문한 적이 없으면
            방문처리
        else:
            건설 불가 처리




'''

#현재 좌표가 이미 방문한 자리인지 확인 -> 함수 호출 전에 확인

def landing_strip_check(idx, land):
    global visited 
    if land[idx-1] == land[idx]:
        return True

    if land[idx-1] == land[idx] - 1:
        if visited[idx-1] == True:
            return False
        visited[idx-1] = True

        for i in range(idx-2, idx-x-1, -1):
            if i < 0:
                return False
            if visited[i] == False and (land[i] == land[i+1]):
                visited[i] = True
            else:
                return False
        return True
    
    elif land[idx-1] - 1 == land[idx]:
        if visited[idx] == True:
            return False
        visited[idx] = True
        
        for i in range(idx+1, idx+x):
            if i == n:
                return False
            if visited[i] == False and (land[i] == land[i-1]):
                visited[i] = True
            else:
                return False
        return True
    
    else:
        return False

for t_c in range(1, int(input()) + 1):
        
    n, x = map(int,input().split())
    grid = []
    grid_vertical = [[0]*n for _ in range(n)]
    result = 0
    for r in range(n):
        line = list(map(int, input().split()))
        grid.append(line)
        for c in range(n):
            grid_vertical[c][r] = line[c]

    for land in grid:
        visited = [False] * n
        is_landing_strip = True
        for i in range(1, n):
            if landing_strip_check(i, land) == False:
                is_landing_strip = False
                break
        if is_landing_strip:
            result += 1
            

    for land in grid_vertical:
        visited = [False] * n
        is_landing_strip = True
        for i in range(1, n):
            if landing_strip_check(i, land) == False:
                is_landing_strip = False
                break
        if is_landing_strip:
            result += 1
            

    print(f"#{t_c} {result}")


